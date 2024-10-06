# Rename and Delete File 


To rename a file, you use the os.rename() function:

```os.rename(src,dst)```

If the src file does not exist, the ```os.rename()``` function raises a ```FileNotFound```error. 

Similarly, if the dst already exists, the ```os.rename()``` function issues a ```FileExistsError``` error.

To avoid an error if the readme.txt doesn’t exist and/or the notes.txt file already exists, we can use the try...except statement:

```
import os

try:
    os.rename('readme.txt', 'notes.txt')
except FileNotFoundError as e:
    print(e)
except FileExistsError as e:
    print(e)
```

[Click here to see complete code](renameFile.py)

To delete a file, we use the remove() function of the os built-in module. 

For example, the following uses the os.remove() function to delete the readme.txt file:


```
import os

os.remove('readme.txt')

```

If the readme.txt file doesn’t exist, the ```os.remove()``` function will issue an error:

```FileNotFoundError```

To avoid the error, we can check the file exists before deleting it like this using os.path.exist() function or is_file() method from the Path class in the pathlib module.

```
import os

filename = 'readme.txt'
if os.path.exists(filename):
    os.remove(filename)
```

Alternatively, we can use the try...except statement to catch the exception if the file doesn’t exist:

```
import os

try:
    os.remove('readme.txt')
except FileNotFoundError as e:
    print(e)
```

[Click here to see complete code](deleteFile.py)