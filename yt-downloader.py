# ----------------------------------- OVERVIEW -----------------------------------

#           Goal: Create a program to download a YouTube videos
#           Objective: Create a progra that downloads a YouTube video from a URL as mp3/mp4 format

# ----------------------------------- TO DO -----------------------------------

# Add option to log into yt so you can download private playlists
# Add functionality to switch between Windows & Mac OS
#

# ----------------------------------- SOURCE CODE -----------------------------------
from datetime import datetime
from pytube import YouTube
from pytube import Playlist
import re
import os


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

start_time = datetime.now()

def menu():
    print("Do you want to download a playlist, videos, or exit? (p/v/e) ")
    userInput = input().lower()

    while True:
        if userInput == 'p':
            playlist()
        elif userInput == 'v':
            videos()
        elif userInput == 'e':
            os._exit(0)

def videos():
    print("Enter the URL of the YouTube VIDEO you want to be downloaded: ")
    url = input()
    youtube = YouTube(url)
    print(youtube.title)

    # mp3 or mp4 download preference
    print("mp3 or mp4? (3/4): ")
    pref = input().lower()
    if pref == 'mp3' or pref == '3':
        video = youtube.streams.filter(only_audio=True).first()
        video.download("C:/Users/Adnan/Desktop") 
    elif pref =='mp4' or pref == '4':
        video = youtube.streams.filter(adaptive=True).first()
        video.download("C:/Users/Adnan/Desktop") 

def playlist():
    playlist=[]

    print("Enter URL of the PLAYLIST: ")
    url = input()

    driver = webdriver.Chrome()
    driver.get(url)

    links = driver.find_elements_by_xpath("//a[@href]")
    for link in links:
        href = link.get_attribute("href")
        if href.startswith('https://www.youtube.com/watch?v='):
            playlist.append(href)

    driver.close()

    playlist = list(dict.fromkeys(playlist))
    print("Length of playlist: " + str((len(playlist) - 1)))

    # First link will be a duplicate with a different URL, because thats how YouTube playlists work
    for l in range(1, len(playlist)):
        print(playlist[l])

    print("zz")


if __name__ == '__main__':
    menu()
    videos()
    playlist()


end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))