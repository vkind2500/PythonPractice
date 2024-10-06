import csv

file_path = 'FileIO/Write CSV File/Resources/countries.csv'
header = ['name', 'area', 'country_code2', 'country_code3']
data = [
    ['Albania', 28748, 'AL', 'ALB'],
    ['Algeria', 2381741, 'DZ', 'DZA'],
    ['American Samoa', 199, 'AS', 'ASM'],
    ['Andorra', 468, 'AD', 'AND'],
    ['Angola', 1246700, 'AO', 'AGO']
]

with open(file_path,'w',encoding='UTF8',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)