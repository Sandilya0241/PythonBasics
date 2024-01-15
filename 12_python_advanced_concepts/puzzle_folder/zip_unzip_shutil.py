# To compress whole folder and extract whole folder, shutil is a better option

from shutil import unpack_archive
from os import getcwd,walk
from re import findall

# unpack_archive("unzip_me_for_instructions.zip","unzip_me_for_instructions","zip")
pattern = r'\d{3}-\d{3}-\d{4}'

for folder, _, files in walk(getcwd() + "\\unzip_me_for_instructions"):
    for file in files:
        with open(folder + "\\" + file,"r") as fp:
            match = findall(pattern,fp.read())

            if(len(match) > 0):
                print(file)
                break