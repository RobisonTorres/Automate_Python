import youtube_downloader
from pathlib import Path
print('Youtube Downloader.')
print()

def directory_path():
    
    # This function determines the download's location.
    directory = (input(r"Type in the directory's path or hit enter to choose the 'Downloads' folder: "))
    downloads = str(Path.home() / "Downloads")
    return directory or downloads

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
    option = input('Press "1" to download video or "2" to download audio: ')

    if option == '1':
        video = input('\nPress "v" to download video or "p" to download playlist: ').lower()
        if video == 'v':
            youtube_downloader.download_video(directory, link = input("Type in the videos's url: "))
        elif video == 'p':
            youtube_downloader.download_playlist(youtube_downloader.download_video, directory, link = input("Type in the playlist's url: "))
        else:
            print('Wrong option.')            
    
    elif option == '2':
        audio = input('Press "a" to download audio or "p" to download playlist: ').lower()
        if audio == 'a':
            youtube_downloader.download_audio(directory, link = input("Type in the videos's url: "))
        elif audio == 'p':
            youtube_downloader.download_playlist(youtube_downloader.download_audio, directory, link = input("Type in the playlist's url: "))
        else:
            print('Wrong option.')   

    else:
        print('Wrong option.')

    repeat()
    return 'Operation finished.'

print(download())