from pytube import YouTube, Playlist
from pathlib import Path
import os
print('Youtube Downloader.')
print()

def directory_path():
    
    # This function determines the download's location.
    directory = (input(r"Type in the directory's path or hit enter to choose the 'Downloads' folder: "))
    downloads = str(Path.home() / "Downloads")
    return directory or downloads

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

def download_playlist(directory, link):

    # This function downloads playlists form YouTube.
    playlist = Playlist(link)
    playlist_videos = list(playlist.video_urls)
    for video in playlist_videos:
        download_audio(directory, video)
    print('All audios has been downloaded.')

def repeat():

    # This function repeats the operation if asked.
    while True:
        option = input('\nPress "y" to continue downloading: ').lower()
        if option != 'y':
            break  
        download()

def download():

    # This function downloads audios or playlists from youtube based on user's input.
    directory = directory_path()
    option = input('Press 1 to download an audio or 2 to download playlist: ')
    if option == '1':
        download_audio(directory, link = input("Type in the videos's url: "))
    elif option == '2':
        download_playlist(directory, link = input("Type in the playlist's url: "))
    else:
        print('Wrong option.')
    repeat()
    return 'Operation finished.'

print(download())