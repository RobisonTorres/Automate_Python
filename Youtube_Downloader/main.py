from youtube_downloader import download_main_video
from youtube_audio import download_main_audio

def main():
    
    choice = input('Press 1 to download videos or 2 to download only audios: ')
    if choice == '1':
        print(download_main_video())
    elif choice == '2':
        print(download_main_audio())
    else:
        print('wrong option!')

main()
