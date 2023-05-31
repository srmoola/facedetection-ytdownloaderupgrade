from pytube import YouTube # imports what we need for pytube
import os # for terminal clear
from time import sleep # for readability

def mainDowload():
    url = ""

    def switchPath(string):
        converted_string = string.replace('\\', '/')
        converted_string = string.replace('"', '')
        return converted_string

    while True:
        
        os.system("cls")

        dummyurl = str(input("Enter Youtube Video URL: "))

        try: 
            my_video = YouTube(dummyurl)
        except Exception as e:
            print("Invalid Youtube URL")
            sleep(2)
            continue

        print(f"\n\nVideo Title: {my_video.title}")
        print(f"View Count: {my_video.views}")
        print(f"Youtuber Name: {my_video.author}")

        check = str(input("\nType yes or Y to continue, anything else to restart: "))

        if check == "yes" or check =="Y":
            url = dummyurl
            break
        else:
            continue

    my_videodownload = YouTube(url)

    my_video= my_videodownload.streams.get_highest_resolution()

    dummy_folder_path = str(input(r"Enter File Path you want to download in: "))

    folder_path = switchPath(dummy_folder_path)

    try:
        my_video.download(output_path=folder_path)
        print("\nDownload Success, check your folder for download!")
    except Exception as e:
        print("Download Failed, Please Retry :( ")


mainDowload()