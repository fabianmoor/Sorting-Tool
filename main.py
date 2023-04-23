import os
import time


dir_path = "/home/fabbem/Downloads/"
dir_music = "/home/fabbem/Downloads/Music/"
dir_pictures = "/home/fabbem/Downloads/Pictures/"
dir_ipa = "/home/fabbem/Downloads/IPA/"


while True:


    filesmusic = [file for file in os.listdir(dir_path) if file.endswith(".mp3") or file.endswith(".mp4")]
    filespictures = [file for file in os.listdir(dir_path) if file.endswith(".png") or file.endswith(".jpeg") or file.endswith(".jpg")]
    filesipa = [file for file in os.listdir(dir_path) if file.endswith(".ipa")]

    for file in filesipa:
        error = os.system(f"ls {dir_ipa} 2>/dev/null")
        if error != 512:
            os.system(f"mv {dir_path}{file} {dir_ipa}")
        else:
            os.system(f"mkdir {dir_ipa}")
            os.system(f"mv {dir_path}{file} {dir_ipa}")
    
    for file in filesmusic:
        error = os.system(f"ls {dir_music} 2>/dev/null")
        if error != 512:
            os.system(f"mv {dir_path}{file} {dir_music}")
        else:
            os.system(f"mkdir {dir_music}")
            os.system(f"mv {dir_path}{file} {dir_music}")
            
    for file in filespictures:
        error = os.system(f"ls {dir_pictures} 2>/dev/null")
        if error != 512:
            os.system(f"mv {dir_path}{file} {dir_pictures}")
        else:
            os.system(f"mkdir {dir_pictures}")
            os.system(f"mv {dir_path}{file} {dir_pictures}")

    time.sleep(0.2)
