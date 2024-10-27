# Python Directory

## Get the current working directory

The current working directory is the directory where the Python script is running. T


```python
import os

cwd = os.getcwd()
print(f'Current Working Directory is {cwd}')
```

    Current Working Directory is /Users/kkumar/Documents/GreatLearning


## Join and split a path

The join() function joins path components together and returns a path with the corresponding path separator. 
For example, it uses backslash (\) on Windows and forward slash (/) on macOS or Linux.


```python
import os

fp = os.path.join('temp', 'python')
print(fp)  # temp\python (on Windows)

pc = os.path.split(fp)
print(pc)  # ('temp', 'python')

```

    temp/python
    ('temp', 'python')


## Test if a path is a directory

To check if a path exists and is a directory, we can use the functions ``os.path.exists()`` and ``os.path.isdir()`` functions. For example:



```python
import os

cwd = os.getcwd()

if os.path.exists(cwd) and os.path.isdir(cwd):
    print(f'{cwd} exist and is directory')
```

    /Users/kkumar/Documents/GreatLearning exist and is directory


## Create a directory

To create a new directory, we use ``os.mkdir()`` function. And we should always check if a directory exists first before creating a new directory.



```python
import os

cwd = os.getcwd()
path = os.path.join(cwd,'new_dir')

if not os.path.exists(path):
    os.makedirs(path)


```

## Rename a directory

To rename the directory, we use the ``os.rename()`` function:


```python
 import os

cwd = os.getcwd()
old_path = os.path.join(cwd,'new_dir')
new_path = os.path.join(cwd,'rename_dir')

if os.path.exists(old_path) and not os.path.exists(new_path):
    os.rename(old_path,new_path)
    print(f'Rename path {old_path} to path {new_path}')
```

    Rename path /Users/kkumar/Documents/GreatLearning/new_dir to path /Users/kkumar/Documents/GreatLearning/rename_dir


## Delete a directory

To delete a directory, we use the ``os.rmdir()`` function as follows:


```python
import os

cwd = os.getcwd()
new_path = os.path.join(cwd,'rename_dir')

if os.path.exists(new_path):
    os.rmdir(new_path)
    print(f'Remove directory : {new_path}')
```

    Remove directory : /Users/kkumar/Documents/GreatLearning/rename_dir


## Traverse a directory recursively

The ``os.walk()`` function allows us to traverse a directory recursively. The ``os.walk()`` function returns the root directory, the sub-directories, and files.


```python
import os

cwd = os.getcwd()
for root,dir,files in os.walk(cwd):
    print(f'{root} has directory {dir} and files {files}')
```

    /Users/kkumar/Documents/GreatLearning has directory ['.ipynb_checkpoints'] and files ['intro_to_python_data_types.ipynb', 'Untitled.ipynb', 'Welcome.ipynb']
    /Users/kkumar/Documents/GreatLearning/.ipynb_checkpoints has directory [] and files ['Welcome-checkpoint.ipynb', 'Untitled-checkpoint.ipynb', 'intro_to_python_data_types-checkpoint.ipynb']


## List Directories and Files in Python

All files and sub-directories inside a directory can be retrieved using the ``listdir()`` method.


```python
import os
os.listdir('.')
```




    ['intro_to_python_data_types.ipynb',
     'Untitled.ipynb',
     '.ipynb_checkpoints',
     'Welcome.ipynb']



## Get Operating System Name

To get operating system , we can use ``os.name()`` command from ``os`` module. 


```python
import os

print(os.name)
```

    posix


#### Note : For window based system, it will print nt and for linux and mac based system - posix
