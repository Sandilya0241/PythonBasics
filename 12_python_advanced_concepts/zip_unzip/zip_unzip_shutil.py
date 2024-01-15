# To compress whole folder and extract whole folder, shutil is a better option

from shutil import make_archive,unpack_archive
from os import getcwd

dir_to_archive = getcwd() + "\\shutil_zip_folder"
output_filename = getcwd() + "\\output\\shutil_zip"

make_archive(output_filename,"zip",dir_to_archive)

unpack_archive(getcwd() + "\\output\\shutil_zip.zip",getcwd() + "\\output\\extract_shutil","zip")

