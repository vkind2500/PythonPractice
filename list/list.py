
# To create the empty list
color = []

# Add item at the end of list
color.append('Cyan')
color.append('Blue')

print(color)

# To find the index of list's element

print(color.index('Blue'))

# To insert element at any position of list

color.insert(1,'Purple')
print(color)

# To check if element exist in list

colorr = 'Purple'

print(f'Color Purple exist in list : {colorr in color}' )

# To remove element at particular index

del color[1]

print(color)

# To pop last element from List

print(f' The last element popped up from list is {color.pop()}')

color.append('Burgundy')
color.append('Magenta')

# To pop up element at index 1

print(f' The 1st element popped up from list is {color.pop(0)}')

# To remove element by value

color.remove('Magenta')

print(color)

