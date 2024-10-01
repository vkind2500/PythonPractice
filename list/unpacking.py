colors = ['red', 'blue', 'green','cyan']

'''

Number of variables on the left side should be same as the number of elements in the list on the right side.
Assigning fewer variables on left will throw an Value Error with the description -  too many values to unpack

'''
red,blue,green,cyan = colors

print(f'Red = {red},Blue = {blue},Green = {green},Cyan = {cyan}')

'''
To unpack the first few elements of a list and don’t care about the other elements
    *   First, unpack the needed elements to variables.
    *   Second, pack the leftover elements into a new list and assign it to another variable.

'''

red,blue,*others = colors

print(f'Red = {red},Blue = {blue},Others = {others}')
