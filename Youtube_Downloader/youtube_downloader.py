from pytube import YouTube, Playlist
from pathlib import Path
print('Youtube Downloader.')
print()

def directory_path():
    
    # This function determines the download's location.
    directory = (input(r"Type in the directory's path or hit enter to choose the 'Downloads' folder: "))
    downloads = str(Path.home() / "Downloads")
    return directory or downloads

def download_video(directory, link):
    
    # This function downloads videos from YouTube.
    youtube_video = YouTube(link, use_oauth=True, allow_oauth_cache=True)
    youtube_video = youtube_video.streams.get_highest_resolution()
    try:
        youtube_video.download(directory)
        print('Download successfully.')
    except: return 'Sorry, something went wrong.'

def download_playlist(directory, link):

    # This function downloads playlists form YouTube.
    playlist = Playlist(link)
    playlist_videos = list(playlist.video_urls)
    for video in playlist_videos:
        download_video(directory, video)
    print('All videos has been downloaded.')

def repeat():

    # This function repeats the operation if asked.
    while True:
        option = input('\nPress "y" to continue downloading: ').lower()
        if option != 'y':
            break  
        download_main_video()

def download_main_video():

    # This function downloads videos or playlists from youtube based on user's input.
    directory = directory_path()
    option = input('Press 1 to download video or 2 to download playlist: ')
    if option == '1':
        download_video(directory, link = input("Type in the videos's url: "))
    elif option == '2':
        download_playlist(directory, link = input("Type in the playlist's url: "))
    else:
        print('Wrong option.')
    repeat()
    return 'Operation finished.'