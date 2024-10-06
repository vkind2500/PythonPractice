import os
from pathlib import Path

src_file = 'FileIO/Write CSV File/Resources/countries.csv'

try:
    path = Path(src_file)
    if path.is_file():
        os.remove(src_file)
    else:
        print('File does not exist')
except FileNotFoundError as e:
    print(e)            
