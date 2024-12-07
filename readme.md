Requirements    

# ffmpeg 
```curl.exe -L -o ffmpeg.zip https://github.com/yt-dlp/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip```

```Expand-Archive -Path ffmpeg.zip -DestinationPath .```

# yt-dlp
```pip install "yt-dlp[default,curl-cffi]"```


# Set up the script:
replace PLAYLIST_URL with your playlist url\
replace CHANNEL_URL with your channel url.\
Adjust the TITLE_KEYWORDS to match your video title patterns.\

# Run the script:
```python ytvod.py```

# Custom Schedule: (idk)
Use cron or Task Scheduler if you want to run it at specific times instead of continuously.(really dont know how this works chatgpt told me so)