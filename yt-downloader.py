# ----------------------------------- OVERVIEW -----------------------------------

#           Goal: Create a program to download a YouTube videos
#           Objective: Create a progra that downloads a YouTube video from a URL as mp3/mp4 format

# ----------------------------------- SOURCE CODE -----------------------------------
from datetime import datetime
from pytube import YouTube #pytube3
from pytube import Playlist
import re

from bs4 import BeautifulSoup as bs
import requests

start_time = datetime.now()

def initialize():
    print('Starting .   .   .')

def one_video():
    print("Enter the URL of the YouTube VIDEO you want to be downloaded: ")
    url = input()
    youtube = YouTube(url)
    print(youtube.title)
    video = youtube.streams.first()
    video.filter(only_audio=True).download("C:/Users/Adnan/Desktop") # Path where to store the video, default is the file where the script is

def playlist():
    print("Enter the URL of the YouTube PLAYLIST you want to be downloaded: ")
    url = input()
    playlist = Playlist(url)
    # playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
    playlist.download_all()
    # for video in playlist:
    #     video.streams.get_highest_resolution().download()

    #playlists don't work, could just use a multiple single URL approach?


def download():
    playlist=[]
    url=input("Enter the Youtube Playlist URL : ") #Takes the Playlist Link
    data= requests.get(url)
    soup=bs4.BeautifulSoup(data)

    for links in soup.find_all('a'):
        link=links.get('href')
        # if (link[0:6]=="/watch" and link[0]!="#"):
        print(link)

    # print(playlist)



if __name__ == '__main__':
    initialize()
    # one_video()
    # playlist()
    download()


end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))