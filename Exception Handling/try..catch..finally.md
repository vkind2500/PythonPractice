# Introduction to Python try…catch…finally statement

The ```try...except``` statement also has an optional clause called finally:

```
try:
    # code that may cause exceptions
except:
    # code that handle exceptions
finally:
    # code that clean up
```

The ```finally``` clause always executes whether an exception occurs or not. And it executes after the ```try``` clause and any ```except``` clause.

### Flowchart

![try..catch..finally](https://www.pythontutorial.net/wp-content/uploads/2020/10/try-except-finally.png)

### [try…catch…finally statement example](try..catch..finally.md)

Output:
```
division by zero
Finishing up.
```
## try…finally statement

The catch clause in the try...catch...finally statement is optional. So we can write it like this:

```
try:
    # the code that may cause an exception
finally:
    # the code that always executes
```    

Typically, you use this statement when you cannot handle the exception but you want to clean up resources. For example, you want to close the file that has been opened.