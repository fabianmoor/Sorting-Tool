import os
import time

dir_path = "/Users/fabbem/Downloads/"
dir_music = "/Users/fabbem/Downloads/Music/"
dir_pictures = "/Users/fabbem/Downloads/Pictures/"
dir_ipa = "/Users/fabbem/Downloads/IPA/"

while True:

    filesmusic = [file for file in os.listdir(dir_path) if file.endswith(".mp3") or file.endswith(".mp4")]
    filespictures = [file for file in os.listdir(dir_path) if file.endswith(".png") or file.endswith(".jpeg") or file.endswith(".jpg")]
    filesipa = [file for file in os.listdir(dir_path) if file.endswith(".ipa")]


    for file in filesmusic:
        file = file.replace(' ', '\ ')
        error = os.system(fr"ls {dir_music} 2>/dev/null")
        
        print(dir_path+file)
        if error != 256:
            os.system(fr"mv {dir_path+file} {dir_music}")
        else:
            os.system(fr"mkdir {dir_music}")
            os.system(fr"mv {dir_path}{file} {dir_music}")

    time.sleep(0.2)
