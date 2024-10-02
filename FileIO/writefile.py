'''

Theory : To write to a text file in Python, you follow these steps:

First, open the text file for writing (or append) using the open() function.
Second, write to the text file using the write() or writelines() method.
Third, close the file using the close() method.
The following shows the basic syntax of the open() function:

f = open(file, mode)
--------------------------------------------------------------------------------------------------------
| Mode  | Description                                                                                   |
| ------|---------------------------------------------------------------------------------------------- |
| 'w'   | Open a text file for writing. If the file exists, the function will truncate all the contents | 
|       | as soon as you open it. If the file doesn’t exist, the function creates a new file.           |
| 'a'   | Open a text file for appending text. If the file exists, the function appends contents        |
|       | at the end of the file.                                                                       |
| '+'   | Open a text file for updating (both reading & writing).                                       |
---------------------------------------------------------------------------------------------------------


'''



'Example 1: The following example shows how to use the write() function to write a list of texts to a text file:'

lines = ['Readme', 'How to write text files in Python']

with open('FileIO/writeme.txt','w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')

'''
If we treat each element of the list as a line, we need to concatenate it with the newline character like this:
'''

with open('FileIO/writeme1.txt','w') as f:
    f.write('\n'.join(lines))


'Example 2: To append to a text file, we need to open the text file for appending mode. '

more_lines = ['', 'Append text files', 'The End']   

with open('FileIO/writeme.txt','a') as f:
    f.write('\n'.join(more_lines))

'''Example 3: Writing UTF-8 Characters to a text file we need to pass parameter encoding='utf8' otherwise it will throw  

UnicodeEncodeError: 'charmap' codec can't encode characters in position 0-44: character maps to <undefined>

'''


quote = '成功を収める人とは人が投げてきたレンガでしっかりした基盤を築くことができる人のことである。'

with open('FileIO/utf8.txt', 'w', encoding='utf-8') as f:
    f.write(quote)


'''

Note - All thses scripts creates a file in the same directory where the script file locates. 
If we want to create a file in a specified directory e.g., docs/readme.text, 
we need to ensure that the docs directory exists before creating the file. Otherwise, 

we’ll get an exception - FileNotFoundError: [Errno 2] No such file or directory: 'docs/readme.txt'

'''

try:
    with open('FileIO/Resources/utf8.txt', 'w', encoding='utf-8') as f:
        f.write(quote)
except FileNotFoundError:
    print('File Not Found')


'''

X mode in file handling : In Python, the x mode in file handling is used to create a new file for writing. 
If the file already exists, it will raise a FileExistsError. 
This mode is useful when you want to ensure that a file is created only if it does not already exist, 
thus preventing accidental overwriting of existing files.

'''

try:
    with open('filename.txt', 'x') as file:
        file.write('Hello, World!')
except FileExistsError:
    print('File Already Exist')


