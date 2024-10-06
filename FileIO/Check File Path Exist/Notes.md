# Python Check If File Exists


When processing files, we’ll often want to check if a file exists before doing something else with it such as reading from the file or writing to it.

To do it, we can use the exists() function from the os.path module or is_file() method from the Path class in the pathlib module.

### os.path.exists() function

```from os.path import exists```

```file_exists = exists(path_to_file)```


### Path.is_file() method

```from pathlib import Path```

```path = Path(path_to_file)```

```path.is_file()```