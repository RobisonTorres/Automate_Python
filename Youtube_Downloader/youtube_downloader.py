from pytube import YouTube, Playlist
from pathlib import Path
print('Youtube Downloader.')
print()

def directory_path():
    
    # This function...
    directory = (input(r"Type in the directory's path or hit enter to choose the 'Downloads' folder: "))
    downloads = str(Path.home() / "Downloads")
    return directory or downloads

def download_video(directory, link):
    
    # This function...
    youtube_video = YouTube(link, use_oauth=True, allow_oauth_cache=True)
    youtube_video = youtube_video.streams.get_highest_resolution()
    try:
        youtube_video.download(directory)
        print('Download successfully.')
    except: return 'Sorry, something went wrong.'

def download_playlist(directory, link):

    # This function...
    playlist = Playlist(link)
    playlist_videos = list(playlist.video_urls)
    for video in playlist_videos:
        download_video(directory, video)
    print('All videos has been downloaded.')

def repeat():

    # This function...
    option = input('\nPress "y" to continue to download: ').lower()
    if option == 'y': return download()

def download():

    # This function...
    directory = directory_path()
    choice = input('Press 1 to download video or 2 to download playlist: ')
    if choice == '1':
        download_video(directory, link = input("Type in the videos's url: "))
    elif choice == '2':
        download_playlist(directory, link = input("Type in the playlist's url: "))
    else:
        print('Wrong option.')
    repeat()
    return 'Operation finished.'

print(download())