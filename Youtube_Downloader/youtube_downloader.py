from pytube import YouTube, Playlist
from pytube.cli import on_progress
from pathlib import Path
import sys, subprocess
subprocess.run('cls', shell=True)
print('Youtube Downloader.')
print()

def download():

    # This function downloads youtube videos.
    start = 'Yes'
    while start == 'Yes':
        option = int(input('Press 1 to download Video or Press 2 to download Playlist: '))
        downloads_path = str(Path.home() / "Downloads")
        print()
        directory = (input(r"Download Location - Type in the directory's path or hit enter to choose the Downloads folder:" + '\n')
                            or downloads_path)

        if option == 1:
            print()
            link = input("Type in the videos's url that you want to download:\n")
            youtube_video = YouTube(link, use_oauth=True, allow_oauth_cache=True, 
                                    on_progress_callback=on_progress)
            youtube_video = youtube_video.streams.get_highest_resolution()
            try:
                youtube_video.download(directory)
                print('Download successfully.')
            except: return 'Sorry, something went wrong.'

        elif option == 2:
            print()
            link = input("Type in the playlist's url that you want to download:\n")
            playlist = Playlist(link)
            playlist_videos = list(playlist.video_urls)
            try:
                for num, video in enumerate(playlist_videos, 1):
                    youtube_video = YouTube(video,  use_oauth=True, allow_oauth_cache=True)
                    youtube_video = youtube_video.streams.get_highest_resolution()
                    youtube_video.download(directory)
                    print('Video ' + str(num) + ' is Downloaded.')
            except: return 'Sorry, something went wrong.'
    
        else:
            return 'Wrong option.'
        print()
        start = input("Type in 'y' if you want to continue or anything else to stop:\n" ).lower()
        subprocess.run('cls', shell=True)
    return 'Operation is finished.'

print(download())
