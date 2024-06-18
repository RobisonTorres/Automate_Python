from pytube import YouTube, Playlist
from pathlib import Path
import os

def download_video(directory, link):
    
    # This function downloads videos from YouTube.
    youtube_video = YouTube(link, use_oauth=True, allow_oauth_cache=True)
    youtube_video = youtube_video.streams.get_highest_resolution()
    try:
        youtube_video.download(directory)
        print('Download successfully.')
    except: return 'Sorry, something went wrong.'

def download_audio(directory, link):
    
    # This function downloads videos from YouTube on format .mp3 and stores on 'Downloads' folder.
    youtube_video = YouTube(link, use_oauth=True, allow_oauth_cache=True)
    youtube_video = youtube_video.streams.get_audio_only()
    try:
        out_file = youtube_video.download(directory)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        print('Download successfully.')
    except: return 'Download successfully.'

def download_playlist(function, directory, link):

    # This function downloads playlists form YouTube.
    playlist = Playlist(link)
    playlist_videos = list(playlist.video_urls)
    for video in playlist_videos:
        function(directory, video)
    print('All videos has been downloaded.')