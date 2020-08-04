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
import getpass
import glob

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

start_time = datetime.now()
def menu():

    username = getpass.getuser()

    print("------------------------------------------------------------------------------------------ ")
    print("----------------------------------    Hello, " + username + "     ----------------------------------- ")
    print("------------------------------------------------------------------------------------------ ")
    print("------------------------------------------------------------------------------------------\n")


    while True:
        userInput = input("Do you want to change your (s)ettings, (c)lear existing files, download a (p)laylist, (v)ideos, (m)usic or (e)xit? ").lower()
        if userInput == 'p':
            playlist()
        elif userInput == 'v':
            videos()
        elif userInput == 's':
            settings()
        elif userInput == 'm':
            music()
        elif userInput == "c":
            clear()
        elif userInput == 'e':
            os._exit(0)

def videos():
    url = input("Enter the URL of the YouTube VIDEO you want to be downloaded: ")
    youtube = YouTube(url)
    print(youtube.title)

    # mp3 or mp4 download preference
    pref = input("mp3 or mp4? (3/4): ").lower()


    if pref == 'mp3' or pref == '3':
        video = youtube.streams.filter(only_audio=True).first()
        video.download("C:/Users/Adnan/Desktop") 
    elif pref =='mp4' or pref == '4':
        video = youtube.streams.first()
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

def settings():
    print("TB developed")


def clear():
    print("C:\Users\Adnan\Documents\GitHub\yt-downloader\data")

def music():
    while True:
        url = input("Enter the URL or (e)xit: ")
        if url == 'e':
            break
        else:
            youtube = YouTube(url)
            print(youtube.title)

            video = youtube.streams.filter(only_audio=True).first()
            file_download = video.download("C:/Users/Adnan/Desktop")
            # changes file to mp3
            os.rename(file_download, file_download[0:-4]  + '.mp3')
            

if __name__ == '__main__':
    menu()

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))