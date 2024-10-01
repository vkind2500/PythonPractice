
# Using intersection method

s1 = {'A','B','C'}
s2 = {'D','C','E'}

print(f'Using set.intersection method -> {set.intersection(s1,s2)}')

# Using & operator

print(f'Using \'&\' operator -> {s1 & s2}')

'''
Difference between intersection method and '&'

    The set intersection operator only allows sets, while the set intersection() method can accept any iterables, like strings, lists, and dictionaries.

'''



