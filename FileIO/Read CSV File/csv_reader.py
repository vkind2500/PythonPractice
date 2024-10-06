from functools import reduce
import csv

file_path = 'FileIO/Read CSV File/Resources/country.csv'


"""

Example 1 : Reading a CSV file examples

"""
# with open(file_path, encoding="utf8") as f:
#     csv_reader = csv.reader(f)
#     for line in csv_reader:
#         print(line)

"""

Example 2 : Skip first line (Header) using enumerate function 

"""  

# with open(file_path, encoding="utf8") as f:
#     csv_reader = csv.reader(f)
#     for line_no,line in enumerate(csv_reader):
#         if line_no == 0:
#             continue
#         else:
#             print(line)

"""

Example 3 : Skip first line (Header) using next() function 

"""

# with open(file_path, encoding="utf8") as f:
#     csv_reader = csv.reader(f)
#     next(csv_reader)
#     for line in csv_reader:
#         print(line)

"""

Example 4 : Read country.csv to calculate total areas of all countries

"""

def calculate_total(a,b):
    return a+b



with open(file_path, encoding="utf8") as f:
    csv_reader = csv.reader(f)
    next(csv_reader)

    country_areas = [float(line[1]) for line in csv_reader]
    # print(country_areas)

    total_area = reduce(calculate_total,country_areas)
    print(f'Total area of all countries in country.csv is {total_area}')