import os
from os import listdir
from os.path import isfile, join
FOLDER_NAME = 'eBOOK PRODUCTION ASSETS'

def get_filenames(mypath):
    file_list = []
    for f in listdir(mypath):
        if isfile(join(mypath, f)):
            file_list.append(f)
    print ('Got file list '+str(file_list)+'. Banging.')
    return file_list

def remove_ext(file_name):
    return os.path.splitext(file_name)[0]

def create_folder(folder_name):
    name_with_path = join(FOLDER_NAME,folder_name)
    is_isbn = len(folder_name) == 13 and folder_name.isnumeric() and not os.path.exists(name_with_path)
    if is_isbn:
        os.makedirs(name_with_path)
        print('Created folder '+folder_name)
        
def move_file(source_file,folder_name):
    if os.path.exists(join(os.getcwd(),FOLDER_NAME,folder_name)):
        old_path = join(os.getcwd(),FOLDER_NAME,source_file)
        new_path = join(os.getcwd(),FOLDER_NAME,folder_name,source_file)
        os.rename(old_path, new_path)
        print('Moved file '+source_file)

mypath = join(os.getcwd(),FOLDER_NAME)
file_list = get_filenames(mypath)
for source_file in file_list:
    folder_name = remove_ext(source_file)
    create_folder(folder_name)
    move_file(source_file,folder_name)
