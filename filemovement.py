import shutil,os,errno

#the challenge is to find a file in a folder or subfolders recursively
#and then get the folder where the file is there
#then move that folder to a specific location which is entered by the user

print("File Search and Folder Movement Utility")

DIRECTORY_TO_SEARCH=input("Please enter the full directory path where the file has to be searched:")
print(f"You entered the path as {DIRECTORY_TO_SEARCH}")
file_to_search=input("Please enter the filename to search:")

def folder_name(name_of_file,DIRECTORY_TO_SEARCH):
    FILE_FOUND = False
    for dirpath, dirname, filenames in os.walk(DIRECTORY_TO_SEARCH):
        for filename in filenames:
            if filename == name_of_file:
                FILE_FOUND = True
                return(os.path.join(dirpath))
                break
    if not FILE_FOUND:
        return -1

folder_path=folder_name(file_to_search,DIRECTORY_TO_SEARCH)

#Getting the folder name from the path
if folder_path != '-1':
    print(f"File is present at Folder path {folder_path}")
    folder_split= folder_path.split("\\")
    folder_split.reverse()
    directory_name=folder_split[0]
    print(f"Folder name is {directory_name}")
else:
    print("File is not present at this location")

TARGET_LOCATION=input("Please enter the full directory path where the folder has to be moved:")
print(f"You entered this path {TARGET_LOCATION}")
COPY_FROM_LOCATION=folder_path
print(f"Source folder to be copied is {COPY_FROM_LOCATION}")
DESTINATION_LOCATION=f"{TARGET_LOCATION}\\{directory_name}"
print(f"Destination folder location is {DESTINATION_LOCATION}")

#if destination folder exists, it is deleted before copying
if os.path.exists(f"{DESTINATION_LOCATION}"):
    print("Path already exists, Deleting the files and folder")
    shutil.rmtree(DESTINATION_LOCATION,ignore_errors=True)
    print("Deleted '%s' directory successfully" % DESTINATION_LOCATION)

#copying the folder and data using copytree commands
try:
    shutil.copytree(COPY_FROM_LOCATION, DESTINATION_LOCATION)
except OSError as err:
    # error caused if the source was not a directory
    if err.errno == errno.ENOTDIR:
        shutil.copy2(COPY_FROM_LOCATION, DESTINATION_LOCATION)
    else:
        print("Error: % s" % err)

if os.path.exists(f"{DESTINATION_LOCATION}"):
    print(f"Files successfully copied to the target location {DESTINATION_LOCATION}")
