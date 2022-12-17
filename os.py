#import os 

#file_path = '/Users/Acer/Desktop/sample/'


#print(file_path)

#if os.path.isfile(file_path):
#    os.remove(file_path)
#    print("File has successfully been deleted!")
#else:
#    print("This file does NOT exist!!!")

import os
import shutil

# Set the path to the parent folder
parent_folder_path = "C:\myfolder"

# Set the names of the folders and files you want to delete
folder_names = ["folder1", "folder2", "folder3"]
file_names = ["file1.txt", "file2.txt", "file3.txt"]

# Delete the folders
for folder_name in folder_names:
    folder_path = os.path.join(parent_folder_path, folder_name)
    try:
        shutil.rmtree(folder_path)
    except OSError as e:
        print("Error: %s : %s" % (folder_path, e.strerror))

# Delete the files
for file_name in file_names:
    file_path = os.path.join(parent_folder_path, file_name)
    try:
        os.remove(file_path)
    except OSError as e:
        print("Error: %s : %s" % (file_path, e.strerror))
