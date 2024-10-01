'''

Lists support the slice notation that allows you to get a sublist from a list:

sub_list = list[begin: end: step]

The begin index defaults to zero. The end index defaults to the length of the list. And the step index defaults to 1.

The begin, end, and step can be positive or negative. Positive values slice the list from the first element to the last element while negative values slice the list from the last element to the first element.

'''

# Python List slice examples


colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
print(f'List - {colors}')

# The begin index is 1, so the slice starts from the 'orange' color. The end index is 4, therefore, the last element of the slice is 'green'.
sub_colors = colors[1:4]

print(f'Sublist containing elements from index 1 to index 3 - {sub_colors}')

# To get the n-first elements from a list

sub_colors = colors[:3]
print(f'First 3 elements from list - {sub_colors}')

# To get the n-last elements of a list, you use the negative indexes.

sub_colors = colors[-3:]
print(f'Last 3 elements from list - {sub_colors}')

# Slice List to get every nth element from a list. Let's say to get every 2nd element from list.

sub_colors = colors[::2]
print(f'Sublist containing every second element - {sub_colors}')

#  Using Python List slice to reverse a list

sub_colors = colors[::-1]
print(f'Sublist containing element in reverse order - {sub_colors}')

# Using Python List slice to substitute part of a list

colors[0:2] = ['Grey','White']
print(f'List after replacement of first two elements - {colors}')

# Python List slice to partially replace and resize a list
colors[0:2] = ['Grey','White','Neon','Brick Red']
print(f'List after replacement of first two elements & adding new elements- {colors}')

# Using Python list slice to delete elements

del colors[2:5]
print(f'List after removing elements from index 2nd to index 4th- {colors}')





