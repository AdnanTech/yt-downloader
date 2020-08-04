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
import shutil

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

start_time = datetime.now()

def menu():
    global directory_path
    directory_path = input("Adnan's Laptop, Macbook or Sameer? (aw/am/s)").lower()

    if directory_path == 'aw':
        directory_path = r"C:\Users\Adnan\Documents\GitHub\yt-downloader\data"
    elif directory_path == 'am':
        directory_path = r"C:\Users\Adnan\Documents\GitHub\yt-downloader\data"
    elif directory_path == 's':
        directory_path = r"C:\Users\Sameer\Desktop"

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

    video = youtube.streams.first()
    video.download(directory_path) 

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
            youtube = YouTube(playlist[l])
            video = youtube.streams.filter(only_audio=True).first()
            file_download = video.download(directory_path)
            # changes file to mp3
            os.rename(file_download, file_download[0:-4]  + '.mp3')

    print("zz")

def settings():
    print("Under development")
    # f = open('directory.txt', "r")
    # print('Your current directory is: ' + f.read())
    # current_dir = f.readline()

    # print(str(current_dir))
    # print(r'"' + str(current_dir) + '\directory.txt"')

    # dir_input = input("Do you want to change download directory? (y/n): ").lower()
    
    # if dir_input == 'y':
    #     new_dir = input("Enter new directory: ")
    #     z = open(('r"' + current_dir + '/directory.txt"'), "w")
    #     z.write('r"' + new_dir + '"')
    #     z.close()
    #     f.close()
    # elif dir_input == 'n':
    #     f.close()



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
        url = input("Enter the URL or (e)xit: ")
        if url == 'e':
            break
        else:
            youtube = YouTube(url)
            print(youtube.title)

            video = youtube.streams.filter(only_audio=True).first()
            file_download = video.download(directory_path)
            # changes file to mp3
            os.rename(file_download, file_download[0:-4]  + '.mp3')
            

if __name__ == '__main__':
    menu()

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))