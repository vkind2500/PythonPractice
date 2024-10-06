
file_path = 'FileIO/Check File Path Exist/Notes.md'

"""
Example 1 : Using os.path.exists() function to check if a file exists

"""


from os.path import exists as file_exist

isFileExist = file_exist(file_path)

print(f'Does file exist : {isFileExist}')

"""

Example 2 : Using the pathlib module to check if a file exists

"""

from pathlib import Path

path = Path(file_path)

if path.is_file() :
    print('File path exist')
else:
    print('File Path not exist')    
