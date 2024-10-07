# try…except

Errors that occur during the execution are called exceptions. 

The causes of exceptions mainly come from the environment where the code executes. 

For example:

1. Reading a file that doesn’t exist.
2. Connecting to a remote server that is offline.
3. Bad user inputs.

To make the program more robust, we need to handle the exception once it occurs. 

In other words, we need to catch the exception and inform users so that they can fix it.

A good way to handle this is not to show what the Python interpreter returns. Instead, we replace that error message with a more user-friendly one.

To do that, we can use the Python ```try...except``` statement:

```
try:
    # code that may cause error
except:
    # handle errors
```    

### Flow Chart

![](https://www.pythontutorial.net/wp-content/uploads/2020/10/Python-try-except.png)

#### Example 1 : [Generic Exception](Example1.py)

If we run the program again and enter the net sales which is not a number, the program will issue the message that we specified in the except block instead:

```
Enter the net sales for
- Prior period:100
- Current period:120'
Error! Please enter a number for net sales.
```

To catch a selected exception, we place the type of exception after the except keyword:

```
try:
    # code that may cause an exception
except <Error Type> as error:
    # code to handle the exception
```

#### Example 2 : [Catch Specific Exception](Example2.py)

When we enter the net sales of the prior period as zero, you’ll get the following message:

```
Enter the net sales for
- Prior period:0
- Current period:100
ZeroDivisionError: float division by zero.
```
## Handling multiple exceptions

The try...except allows us to handle multiple exceptions by specifying multiple except clauses:

```
try:
    # code that may cause an exception
except Exception1 as e1:
    # handle exception
except Exception2 as e2:
    # handle exception
except Exception3 as e3:
    # handle exception 
```

If we want to have the same response to some types of exceptions, you can group them into one except clause:

```
try:
    # code that may cause an exception
except (Exception1, Exception2):
    # handle exception
```

#### Example 3 : [Catch Multiple Exception](Example3.py)


