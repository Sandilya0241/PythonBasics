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