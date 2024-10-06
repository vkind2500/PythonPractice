import csv

file_path = 'FileIO/Read CSV File/Resources/country.csv'

"""

Example 1 : Reading a CSV file using Dict_reader

"""
# with open(file_path, encoding="utf8") as f:
#     csv_reader = csv.DictReader(f)
    
#     next(csv_reader)

#     for line in csv_reader:
#         print(f'The area of {line['name']} is {line['area']} km2')


"""

Example 2 : Reading a CSV file using Dict_reader and custom field names

"""

with open(file_path, encoding="utf8") as f:
    
    fieldnames = ['Name', 'Area', 'Code2', 'Code3']
    csv_reader = csv.DictReader(f,fieldnames)

    
    
    next(csv_reader)

    for line in csv_reader:
        print(f'The area of {line['Name']} is {line['Area']} km2')

