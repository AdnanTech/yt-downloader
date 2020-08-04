# ----------------------------------- OVERVIEW -----------------------------------

#           Goal: Create a program to download a YouTube videos
#           Objective: Create a progra that downloads a YouTube video from a URL as mp3/mp4 format

# ----------------------------------- SOURCE CODE -----------------------------------
from datetime import datetime
from pytube import YouTube #pytube3
from pytube import Playlist
import re


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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

    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/playlist?list=PLcYK4PlHbZQvbWClI38SfOjBt3godBsY1")

    links = driver.find_elements_by_xpath("//a[@href]")
    for link in links:
        href = link.get_attribute("href")
        if href.startswith('https://www.youtube.com/watch?v='):
            playlist.append(href)

    playlist = list(dict.fromkeys(playlist))
    print(len(playlist))
   
    for a in playlist:
        print(a)

    # First link will be a duplicate with a different URL, because thats how YouTube playlists work
    for l in range(1, len(playlist)):

    print("zz")


if __name__ == '__main__':
    initialize()
    # one_video()
    # playlist()
    download()


end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))