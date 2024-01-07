from pytube import YouTube
from pathlib import Path
import os
print('Youtube Downloader.')
print()

def download():

    # This function converts videos into mp3.
    link = input("Type in the videos's url that you want to download:\n")
    youtube_video = YouTube(link, use_oauth=True, allow_oauth_cache=True)
    youtube_video = youtube_video.streams.get_audio_only()
    try:
        out_file = youtube_video.download(str(Path.home() / "Downloads"))
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
    except: return 'Sorry, something went wrong.'
    return 'Download successfully.'

print(download())
