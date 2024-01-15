# CREATE FILES TO BE COMPRESSED

import os
from zipfile import ZipFile,ZIP_DEFLATED


# CREATING SAMPLE FILES
with open(os.getcwd() + "\\file_one.txt", "w+") as fp:
    fp.write("ONE FILE")

with open(os.getcwd() + "\\file_two.txt", "w+") as fp:
    fp.write("TWO FILE")


# COMPRESS FILES
with ZipFile(os.getcwd() + "\\output\\compress.zip","w") as zfp:
    zfp.write("file_one.txt",compress_type=ZIP_DEFLATED)
    zfp.write("file_two.txt",compress_type=ZIP_DEFLATED)


# UNCOMPRESS FILES
with ZipFile(os.getcwd() + "\\output\\compress.zip","r") as zfp:
    zfp.extractall(os.getcwd() + "\\output\\extracted_content")
