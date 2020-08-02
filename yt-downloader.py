# ----------------------------------- OVERVIEW -----------------------------------

#           Goal: Create a program to download a YouTube videos
#           Objective: Create a progra that downloads a YouTube video from a URL as mp3/mp4 format

# ----------------------------------- SOURCE CODE -----------------------------------
from datetime import datetime
from pytube import YouTube #pytube3
from pytube import Playlist

start_time = datetime.now()

def initialize():
    print('Starting .   .   .')

def one_video():
    print("Enter the URL of the YouTube VIDEO you want to be downloaded: ")
    url = input()
    youtube = YouTube(url)
    video = youtube.streams.first()
    video.download("C:/Users/Adnan/Desktop") # Path where to store the video

def playlist():
    print("Enter the URL of the YouTube PLAYLIST you want to be downloaded: ")
    url = input()
    playlist = Playlist(url)
    for video in playlist:
     	video.streams.download()

if __name__ == '__main__':
    initialize()
    one_video()


end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))