s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}

# To find symmetric difference using set.symmetric_difference method

print(f'Symmetric Difference of s1 and s2 using set.symmetric_difference is {set.symmetric_difference(s1,s2)}')

# Using '^' operator

print(f'Symmetric Difference of s1 and s2 using \'^\' is {s1^s2}')

'''
    * The symmetric_difference() method accepts one or more iterables that can be strings, lists, or dictionaries.
    *the symmetric difference operator (^) only applies to sets. If you use it with the iterables which aren’t sets, you’ll get an error. For example:

    scores = {7, 8, 9}
    ratings = [8, 9, 10]
    new_set = scores ^ ratings

    print(new_set)

    Error:

    TypeError: unsupported operand type(s) for ^: 'set' and 'list'

'''




