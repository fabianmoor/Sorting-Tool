import os


fileextensions = [file for file in os.listdir("/home/fabbem/Downloads/")] 

new = fileextensions[0].split(".")

print("." + new[-1])

