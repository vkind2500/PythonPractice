import csv

file_path = 'FileIO/Write CSV File/Resources/countries.csv'
header = ['name', 'area', 'country_code2', 'country_code3']
data = ['Afghanistan', 652090, 'AF', 'AFG']

with open(file_path,'w',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    
    writer.writerow(data)