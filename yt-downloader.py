# ----------------------------------- OVERVIEW -----------------------------------

#           Goal: Create a program to download a YouTube videos
#           Objective: Create a progra that downloads a YouTube video from a URL as mp3/mp4 format

# ----------------------------------- SOURCE CODE -----------------------------------
from datetime import datetime
from pytube import YouTube #pytubee3

start_time = datetime.now()

def initialize():
    print('Starting .   .   .')

def yt():
    print("Enter the URL of the YouTube video you want to be downloaded: ")
    url = input()
    YouTube(url).streams[0].download()


if __name__ == '__main__':
    initialize()
    yt()


end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))