# Introduction to the Python try…except…else statement

The ```try``` statement has an optional ```else``` clause with the following syntax:

```
try:
    # code that may cause errors
except:
    # code that handle exceptions
else:
    # code that executes when no exception occurs
```    

The ```try...except...else``` statement works as follows:

If an exception occurs in the ```try``` clause, Python skips the rest of the statements in the ``try`` clause and the ``except`` statement execute.

In case no exception occurs in the ``try`` clause, the ``else`` clause will execute.

When we include the ```finally``` clause, the ``else`` clause executes after the ``try`` clause and before the ``finally`` clause.

### Example

#### [Evalute BMI example using try..except..else](Example5.py)

#### [try...except...else...finally](Example6.py)