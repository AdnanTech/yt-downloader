# ----------------------------------- OVERVIEW -----------------------------------

#           Goal: Create a program to download a YouTube videos
#           Objective: Create a progra that downloads a YouTube video from a URL as mp3/mp4 format

# ----------------------------------- TO DO -----------------------------------

# Add option to log into yt so you can download private playlists
# Add functionality to switch between Windows & Mac OS

# ----------------------------------- DEV PRE REQUISITES -----------------------------------

# Install libraries pytube3, selenium
# Install chrome driver
# change cipher in the library pytube3
# https://stackoverflow.com/questions/62098925/why-my-youtube-video-downloader-only-downloads-some-videos-and-for-other-videos
# change line 'cipher' to 'signatureCipher' in line 301 of extract.py in the library folder


# ----------------------------------- SOURCE CODE -----------------------------------
from datetime import datetime
from pytube import YouTube
from pytube import Playlist
import re
import os
import getpass
import shutil
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def menu():
    while True:
        username = getpass.getuser()
        global directory_path
        directory_path = input("Current directory or desktop? (d/c): ").lower()
        if directory_path == 'd' or directory_path == 'c':
            # Default dir is the folder
            if directory_path == 'd':
                current_working_directory = os.getcwd()
                current_working_directory = current_working_directory + '\\data'
                directory_path = current_working_directory
                print(current_working_directory)
            elif directory_path == 'c':
                directory_path = r"C:\Users" + '\\' + username + '\\' + r"Desktop"
                print(directory_path)
            break


    print("\n------------------------------------------------------------------------------------------ ")
    print("----------------------------------    Hello, " + username + "     ----------------------------------- ")
    print("------------------------------------------------------------------------------------------\n")


    while True:
        userInput = input("Do you want to (c)lear existing files, download a (p)laylist, (v)ideos, (m)usic or (e)xit: ").lower()
        if userInput == 'p':
            playlist()
        elif userInput == 'v':
            videos()
        elif userInput == 'm':
            music()
        elif userInput == "c":
            clear()
        elif userInput == 'e':
            os._exit(0)

def videos():
    while True:
        try:
            url = input("Enter the URL or (e)xit: ")
            if url == 'e':
                break
            else:
                youtube = YouTube(url)
                print(youtube.title)

                video = youtube.streams.first()
                name_pref = input("Do you want to rename these files? (y/n): ")

                if name_pref == 'y':
                    new_file_name = input("New file name: ")
                    video = youtube.streams.filter(res="720p").first()
                    video.download(directory_path)
                    file_download = video.download(directory_path)
                    print((new_file_name  + '.mp4'))
                    os.rename(file_download, (directory_path + '\\' + new_file_name  + '.mp4'))
                elif name_pref == 'n':
                    video = youtube.streams.filter(res="720p").first()
                    video.download(directory_path) 
        except:
            print("An error has occured")
            break

def playlist():
    try:
        playlist=[]

        url = input("Enter URL of the PLAYLIST: ")

        driver = webdriver.Chrome()
        driver.get(url)
        links = driver.find_elements_by_xpath("//a[@href]")
        for link in links:
            href = link.get_attribute("href")
            if href.startswith('https://www.youtube.com/watch?v='):
                playlist.append(href)
        driver.close()

        #Gets rid of duplicate links
        playlist = list(dict.fromkeys(playlist))
        print("Length of playlist: " + str((len(playlist) - 2)))

        # outputs all the links in the playlist
        # for x in playlist:
        #     print(x)

        # First link will be a duplicate with a different URL, because thats how YouTube playlists work
        # The algorithm of collecting a playlist is abstract, the beginning of every scrape there are 2 links that are songs,
        # but not actually indexed to the playlist, so we start from the third link, which is the beginning of the playlist

        name_pref = input("Do you want to rename these files? (y/n): ")

        if name_pref == 'y':
            for l in range(2, len(playlist)):
                    youtube = YouTube(playlist[l])
                    print(youtube.title)
                    video = youtube.first()
                    file_download = video.download(directory_path)
                    new_file_name = input("New file name: ")
                    print((new_file_name  + '.mp3'))
                    # changes file to mp3
                    os.rename(file_download, (directory_path + '\\' + new_file_name  + '.mp3'))
                    try:
                        os.remove(file_download)
                    except:
                        pass
        elif name_pref == 'n':
            for l in range(2, len(playlist)):
                    youtube = YouTube(playlist[l])
                    # print(youtube.title + ' - ' + playlist[l])
                    print(youtube.title)
                    video = youtube.streams.filter(only_audio=True).first()
                    file_download = video.download(directory_path)
                    # changes file to mp3
                    os.rename(file_download, file_download[0:-4]  + '.mp3')
        print("Playlist downloaded successfully")
    except:
        print("An error occurred.")

def clear():
    dirpath = directory_path
    try:
        for filename in os.listdir(dirpath):
            filepath = os.path.join(dirpath, filename)
            try:
                shutil.rmtree(filepath)
            except OSError:
                os.remove(filepath)
    except:
        print("No files are in the folder.")

def music():
    while True:
        try:
            url = input("Enter the URL or (e)xit: ")
            if url == 'e':
                break
            else:
                youtube = YouTube(url)
                print(youtube.title)

                video = youtube.streams.filter(only_audio=True).first()
                file_download = video.download(directory_path)
                name_pref = input("Do you want to rename this files (y/n): ")

                if name_pref == 'y':
                    new_file_name = input("New file name: ")
                    print((new_file_name  + '.mp3'))
                    os.rename(file_download, (directory_path + '\\' + new_file_name  + '.mp3'))
                elif name_pref == 'n':
                    os.rename(file_download, file_download[0:-4]  + '.mp3')
        except:
            print("An error occurred")
            break


if __name__ == '__main__':
    menu()