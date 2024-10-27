# Working with Files

The ``os.walk()`` function generates file names in a directory by walking the tree either top-down or bottom-up. 

The ``os.walk()`` function yields a tuple with three fields (dirpath, dirnames, and filenames) for each directory in the directory tree.

The following example shows how to use the ``os.walk()`` function to list all files with extension '.ipynb' from the current directory:


```python
import os

ext = '.ipynb'
path = os.getcwd()

jupyter_files = []

for dirpath, dirnames, filenames in os.walk(path):
    for filename in filenames:
        if filename.endswith(ext):
            jupyter_files.append(os.path.join(dirpath, filename))

for file in jupyter_files:
    print(file)
```

    /Users/kkumar/Documents/GreatLearning/intro_to_python_data_types.ipynb
    /Users/kkumar/Documents/GreatLearning/Untitled.ipynb
    /Users/kkumar/Documents/GreatLearning/introduction to os commands.ipynb
    /Users/kkumar/Documents/GreatLearning/Welcome.ipynb
    /Users/kkumar/Documents/GreatLearning/.ipynb_checkpoints/introduction to os commands-checkpoint.ipynb
    /Users/kkumar/Documents/GreatLearning/.ipynb_checkpoints/Welcome-checkpoint.ipynb
    /Users/kkumar/Documents/GreatLearning/.ipynb_checkpoints/Untitled-checkpoint.ipynb
    /Users/kkumar/Documents/GreatLearning/.ipynb_checkpoints/intro_to_python_data_types-checkpoint.ipynb



```python

```
