import time
import os
import datetime
from yt_dlp import YoutubeDL

# User config
PLAYLIST_URL = "" #playlist url as needed
CHANNEL_URL = "" # channel url as needed
OUTPUT_DIR = ""  # change directory as needed, defaults to root of .py
TITLE_KEYWORDS = ["",""]
# user config

CHECK_INTERVAL = 3600
ARCHIVE_FILE = "downloaded_videos.txt"
todays_date = datetime.datetime.now().strftime("%Y%m%d")

if not os.path.exists(ARCHIVE_FILE):
    open(ARCHIVE_FILE, "a").close()


def video_matches_title(title):
    return any(keyword.lower() in title.lower() for keyword in TITLE_KEYWORDS)


def download_video(video_url):
    ydl_opts = {
        "outtmpl": os.path.join(OUTPUT_DIR, "%(title)s_" + todays_date + ".%(ext)s"),
        "download_archive": ARCHIVE_FILE,
        "embed_metadata": True,
        "embed_thumbnail": True,
        "format": "best",
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
    except Exception as e:
        print(f"Download error: {e}")


def check_source(source_url):
    ydl_opts = {
        "quiet": True,
        "extract_flat": True,
        "force_generic_extractor": True,
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            source_info = ydl.extract_info(source_url, download=False)

        new_videos = []
        for entry in source_info.get("entries", []):
            video_title = entry.get("title", "")
            video_url = entry.get("url", "")
            video_date = entry.get("upload_date", "")

            if video_date != todays_date:
                continue

            if video_matches_title(video_title):
                new_videos.append(video_url)

        return new_videos
    except Exception as e:
        print(f"Source check error for {source_url}: {e}")
        return []


def main():
    # main loop to monitor the playlist and channel and if any, download matching videos.
    while True:
        try:
            # check both the playlist and the channel for new videos
            new_videos = check_source(PLAYLIST_URL) + check_source(CHANNEL_URL)

            # remove duplicates while preserving order
            new_videos = list(dict.fromkeys(new_videos))

            if new_videos:
                print(f"Found {len(new_videos)} new videos.")
                for video_url in new_videos:
                    download_video(video_url)
            else:
                print("No new videos found.")
        except Exception as e:
            print(f"Error: {e}")

        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    main()
