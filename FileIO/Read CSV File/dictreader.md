# Reading a CSV file using the DictReader class

When we use the ```csv.reader()``` function, we can access values of the CSV file using the bracket notation such as ```line[0]```, ```line[1]```, and so on. However, using the ```csv.reader()``` function has two main limitations:

However it would be more expressive if we can access the country name like ```line['country_name']```.

Second, when the order of columns from the CSV file is changed or new columns are added, we need to modify the code to get the right data.

This is where the ```DictReader``` class comes into play. 

The DictReader class also comes from the csv module.

The ```DictReader``` class allows us to create an object like a regular CSV reader. 

But it maps the information of each line to a dictionary (dict) whose keys are specified by the values of the first line.

By using the DictReader class, we can access values in the country.csv file like ```line['name']```, ```line['area']```, ```line['country_code2']```, and ```line['country_code3']```.

or if we want to have different field names other than the ones specified in the first line, we can explicitly specify them by passing a list of field names to the DictReader() constructor like this:

```fieldnames = ['country_name', 'area', 'code2', 'code3']```

[Dict Reader Example](../Read%20CSV%20File/dict_reader.py)