'Example 1 : The following example illustrates how to use the read() method to read all the contents of the file into a string:'

print()
print(f'******Read all content of file using read() method******')
print()

with open('FileIO/readme.txt','r') as f:
    contents = f.read()
    print(contents)

'Example 2 : The following example uses the readlines() method to read the text file and returns the file contents as a list of strings:'

print()
print(f'******Read all content of file using readlined() method******')
print()

with open('FileIO/readme.txt','r') as f:
    [print(line) for line in f.readlines()]

'''Note : The reason you see a blank line after each line from a file is that each line in the text file has a newline character (\n). 
To remove the blank line, you can use the strip() method.'''  

print()
print(f'******Read all content of file using readlines() method & stripping newline character ******')
print()


with open('FileIO/readme.txt','r') as f:
    [print(line.strip()) for line in f.readlines()]      

'Example 3: The following example shows how to use the readline() to read the text file line by line:'

print()
print(f'******Read all content of file using readlines() method by using while loop ******')
print()


with open('FileIO/readme.txt','r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        print(line.strip())

'''Example 4: A more concise way to read a text file line by line
The open() function returns a file object which is an iterable object. 
Therefore, you can use a for loop to iterate over the lines of a text file as follows:
'''

print()
print(f'******Read all content of file using file object iterable and for loop ******')
print()


with open('FileIO/readme.txt') as f:
    for line in f:
        print(line.strip())

'''Example 5 : Read UTF-8 text files
The code in the previous examples works fine with ASCII text files. 
However, if you’re dealing with other languages such as Japanese, Chinese, and Korean, the text file is not a simple ASCII text file. And it’s likely a UTF-8 file that uses more than just the standard ASCII text characters.
To open a UTF-8 text file, you need to pass the encoding='utf-8' to the open() function to instruct it to expect UTF-8 characters from the file.
'''



print()
print(f'******Read UTF-8 file ******')
print()


with open('quotes.txt',encoding='utf8') as f:
    for line in f:
        print(line.strip())