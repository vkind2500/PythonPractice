import os

src_file = 'FileIO/Write CSV File/Resources/countries.csv'
dest_file = 'FileIO/Write CSV File/Resources/countries2.csv'

try:
    os.rename(src_file,dest_file)
except FileNotFoundError as e:
    print(e)
except FileExistsError as e:
    print(e)    

