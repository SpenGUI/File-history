import shutil
import os
import datetime

# Get the current date in YYYY-MM-DD format
date = datetime.date.today().strftime('%Y-%m-%d')

# Set the source folder path
source_folder = '/path/to/source/folder'

# Set the destination folder path with the date appended to the folder name
destination_folder = f'/path/to/destination/folder_{date}'

# Create the destination folder if it does not exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Set the file name that contains the folder names to copy
folders_file = 'Folders.txt'

# Read the folders to copy from the file
with open(os.path.join(source_folder, folders_file), 'r') as f:
    folders = f.read().splitlines()

# Copy each folder to the destination folder
for folder in folders:
    shutil.copytree(os.path.join(source_folder, folder), os.path.join(destination_folder, folder))
