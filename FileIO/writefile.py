
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


        
   