# Python Read CSV File

### Reading a csv file in Python

#### To read a CSV file in Python, we follow these steps:

1. Import the csv module:

    ```import csv```

2. Open the CSV file using the built-in ```open()``` function in the read mode:

    ```f = open('path/to/csv_file')```

    ##### If the CSV contains UTF8 characters, we need to specify the encoding like this:

    ```f = open('path/to/csv_file', encoding='UTF8')```

3. Pass the file object (f) to the reader() function of the csv module. The reader() function returns a csv reader object:

    ```csv_reader = csv.reader(f)```

4. The csv_reader is an iterable object of lines from the CSV file. Therefore, we can iterate over the lines of the CSV file using a for loop:

        for line in csv_reader:
            print(line)

    ##### Each line is a list of values. To access each value, we use the square bracket notation []. The first value has an index of 0. The second value has an index of 1, and so on.

    ##### For example, the following accesses the first value of a particular line:

    ````line[0]````

5. Finally, always close the file once we’re no longer access it by calling the close() method of the file object:

    ````f.close()````    

It’ll be easier to use the with statement so that we don’t need to explicitly call the close() method.

#### The following illustrates all above steps for reading a CSV file using ````with```` statement

```import csv

with open('path/to/csv_file', 'r') as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:
        # process each line
        print(line)
```
Output:

```
['name', 'area', 'country_code2', 'country_code3']
['Afghanistan', '652090.00', 'AF', 'AFG']
['Albania', '28748.00', 'AL', 'ALB']
['Algeria', '2381741.00', 'DZ', 'DZA']
['American Samoa', '199.00', 'AS', 'ASM']
...        
```

