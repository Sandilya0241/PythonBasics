
# - OS Modules and DateTime
# =============================================================================================

#     We already know how to open an individual file with Python, but still don't know how to do few things like:
#         - Open every file in a directory.
#         - Want to move files across our computer.

#     Python's os module and shutil allow us to easily navigate files and directories on the computer and then perform actions on them, such as moving them or deleting them.
    
#     The os module provides 3 methods for deleting files:
#         - os.unlink(path) which deletes a file at the path your provide
#         - os.rmdir(path) which deletes a folder (folder must be empty) at the path your provide
#         - shutil.rmtree(path) this is the most dangerous, as it will remove all files and folders contained in the path. 

#     All of these methods can not be reversed! Which means if you make a mistake you won't be able to recover the file. Instead we will use the send2trash module. A safer alternative that sends deleted files to the trash bin instead of permanent removal. ___

#     Install the send2trash module with:
#         - pip install send2trash

import os
import shutil
import send2trash

def file_write():
    fp = open("practice.txt","w+")
    fp.write("This is a test line")
    fp.close()


# file_write()


def os_module():
    # To get current working directory
    print(os.getcwd())
    print()

    # To get list of directories
    print(os.listdir())
    print()

    # To get list of directories from a different path
    print(os.listdir("C:\\Users\\saakh\\Learning\\LearnPython\\PythonBasics\\"))
    print()


# os_module()
    

def move_copy_files():
    # shutil.move("practice.txt","C:\\Users\\saakh\\Learning\\LearnPython\\")
    # print(os.listdir("C:\\Users\\saakh\\Learning\\LearnPython\\"))

    # shutil.move("C:\\Users\\saakh\\Learning\\LearnPython\\practice.txt",os.getcwd())
    # send2trash.send2trash("practice.txt")
    file_path = "C:\\Users\\saakh\\Learning\\LearnPython\\PythonBasics\\12_python_advanced_concepts\\Example_Top_Level"
    for folder, sub_folders, files in os.walk(file_path):
        print(f"Currently looking at {folder}\n")
        print("The sub folders are : ")
        for sub_folder in sub_folders:
            print(f"\t Sub folder : {sub_folder}")
        print()
        for file in files:
            print(f"\t File : {file}")
        print()

move_copy_files()