'''

Syntax : {expression for element in set if condition}

'''

tags = {'Django', 'Pandas', 'Numpy'}
lowercase_tags = {tag.lower() for tag in tags}

print(lowercase_tags)

# To convert all elements of the tags set to lowercase except for the Numpy.

new_tags = {tag.lower() for tag in tags if tag !='Numpy'}

print(new_tags)
