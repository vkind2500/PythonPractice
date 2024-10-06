# Steps for writing a CSV file

#### To write data into a CSV file, we follow these steps:

1. Open the CSV file for writing (w mode) by using the open() function.
2. Create a CSV writer object by calling the writer() function of the csv module.
3. Write data to CSV file by calling the writerow() or writerows() method of the CSV writer object.
4. Close the file once we complete writing data to it.

##### The following code illustrates the above steps:

```import csv

# open the file in the write mode

with open('path/to/csv_file', 'w', encoding='UTF8') as f:
    
    # create the csv writer
    writer = csv.writer(f)

    # write a row to the csv file
    writer.writerow(row)
```

#### [Please see the complete code here](writerow.py)

If we see blank line between two subsequent rows like below

![](<Images/Screenshot 2024-10-06 at 11.39.25 PM.png>)

we can pass the keyword argument newline='' to the open() function as follows:

```open('path/to/csv_file', 'w', encoding='UTF8', newline='')```

### Writing multiple rows to CSV files

To write multiple rows to a CSV file at once, we use the ```writerows()``` method of the CSV writer object.

The following example uses ```writerows()``` method to write multiple rows into the countries.csv file:

[Write Multiple Rows In CSV Example](writerows.py)