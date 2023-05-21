import os
import time

dir_path = "/Users/fabbem/Downloads/"
dir_music = "/Users/fabbem/Downloads/MUSIC/"
dir_pictures = "/Users/fabbem/Downloads/PICTURES/"
dir_ipa = "/Users/fabbem/Downloads/IPA/"
dir_zip = "/Users/fabbem/Downloads/ZIP/"
dir_dmg = "/Users/fabbem/Downloads/DMG/"
dir_torrent = "/Users/fabbem/Downloads/TORRENT/"
dir_pkg = "/Users/fabbem/Downloads/PKG/"
dir_oth = "/Users/fabbem/Downloads/OTHERS/"

filetypes = [".mp3", ".mp4", ".m4a", ".wav", ".asd", ".png", ".jpeg", ".jpg", ".HEIC", ".ipa", ".zip", ".dmg", ".torrent", ".pkg"]

while True:

    filesmusic = [file for file in os.listdir(dir_path) if file.endswith(".mp3") or file.endswith(".mp4") or file.endswith(".m4a") or file.endswith(".wav") or file.endswith(".asd")]
    filespictures = [file for file in os.listdir(dir_path) if file.endswith(".png") or file.endswith(".jpeg") or file.endswith(".jpg") or file.endswith(".HEIC")]
    filesipa = [file for file in os.listdir(dir_path) if file.endswith(".ipa")]
    fileszip = [file for file in os.listdir(dir_path) if file.endswith(".zip")]
    filesdmg = [file for file in os.listdir(dir_path) if file.endswith(".dmg")]
    filestorrent = [file for file in os.listdir(dir_path) if file.endswith(".torrent")]
    filespkg = [file for file in os.listdir(dir_path) if file.endswith(".pkg")]
    filesoth = [file for file in os.listdir(dir_path) if all(not file.endswith(ext) for ext in filetypes) and not os.path.isdir(os.path.join(dir_path, file))]



    for file in filespkg:
        file = file.replace(' ', '\ ')
        error = os.system(f"ls {dir_pkg} 2>/dev/null")
        if error != 256:
            os.system(f"mv {dir_path}{file} {dir_pkg}")
        else:
            os.system(f"mkdir {dir_pkg}")
            os.system(f"mv {dir_path}{file} {dir_pkg}")
    

    for file in filestorrent:
        file = file.replace(' ', '\ ')
        error = os.system(f"ls {dir_torrent} 2>/dev/null")
        if error != 256:
            os.system(f"mv {dir_path}{file} {dir_torrent}")
        else:
            os.system(f"mkdir {dir_torrent}")
            os.system(f"mv {dir_path}{file} {dir_torrent}")

    for file in filesdmg:
        file = file.replace(' ', '\ ')
        error = os.system(f"ls {dir_dmg} 2>/dev/null")
        if error != 256:
            os.system(f"mv {dir_path}{file} {dir_dmg}")
        else:
            os.system(f"mkdir {dir_dmg}")
            os.system(f"mv {dir_path}{file} {dir_dmg}")
        

    for file in fileszip:
        file = file.replace(' ', '\ ')
        error = os.system(f"ls {dir_zip} 2>/dev/null")
        if error != 256:
            os.system(f"mv {dir_path}{file} {dir_zip}")
        else:
            os.system(f"mkdir {dir_zip}")
            os.system(f"mv {dir_path}{file} {dir_zip}")

    for file in filesipa:
        file = file.replace(' ', '\ ')
        error = os.system(f"ls {dir_ipa} 2>/dev/null")
        if error != 256:
            os.system(f"mv {dir_path}{file} {dir_ipa}")
        else:
            os.system(f"mkdir {dir_ipa}")
            os.system(f"mv {dir_path}{file} {dir_ipa}")
    
    for file in filesmusic:
        file = file.replace(' ', '\ ')
        error = os.system(f"ls {dir_music} 2>/dev/null")
        if error != 256:
            os.system(f"mv {dir_path}{file} {dir_music}")
        else:
            os.system(f"mkdir {dir_music}")
            os.system(f"mv {dir_path}{file} {dir_music}")
            
    for file in filespictures:
        file = file.replace(' ', '\ ')
        error = os.system(f"ls {dir_pictures} 2>/dev/null")
        if error != 256:
            os.system(f"mv {dir_path}{file} {dir_pictures}")
        else:
            os.system(f"mkdir {dir_pictures}")
            os.system(f"mv {dir_path}{file} {dir_pictures}")

    for file in filesoth:
        file = file.replace(' ', '\ ')
        error = os.system(f"ls {dir_oth} 2>/dev/null")
        if error != 256:
            os.system(f"mv {dir_path}{file} {dir_oth}")
        else:
            os.system(f"mkdir {dir_oth}")
            os.system(f"mv {dir_path}{file} {dir_oth}")
    
    time.sleep(1)
