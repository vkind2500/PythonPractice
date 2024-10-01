'''
A set is an -
    * Unordered collection of Element
    * All Elements in a set are Unique
    * Elements in a Set cannot be changed.
    * List and Dictionaries are mutable hence they cannot be part of Set Elements

'''


# Define Empty Set

color_set = set() # An empty set evaluates to False in Boolean context.

if not color_set:
    print('Empty Set are falsy')

# To create set from list

skills = set(['Problem Solving','Critical Thinking','Critical Thinking'])
print(skills) # Set function remove duplicate element

# To create character set from String

characters = set("Hello")
print(characters)

# To get number of elements in set
print(f'Number of characters in the set are {len(characters)}')

# To check element present in set

ratings = {1,2,3,4,5}
rating = 4

print(f'Is Rating 4 present in ratings set -> {rating in ratings}')

# To negate the in operator, we use the not operator.

print(f'Rating Set contains ratings 4 -> {rating not in ratings}')

# Add Element in Set

ratings.add(6)

print(ratings)

# Remove element from set

ratings.remove(3)

print(ratings)

# Note : Removing 3 element again using ratings.remove(3) will throw Key Error:3

# ratings.remove(3)



# Discard method

ratings.discard(3) # It will not raise error if element does not exist in set else it removes the element

# Remove and return element . Since set does not have any order, it will remove unspecified element

ratings = {11,2,3,4,5}
rating = ratings.pop()

print(ratings)
print(f'Remove element from set using pop -> {rating}')

# To remove all elements

ratings.clear()
print(ratings)

'''

To make a set immutable, we use the built-in function called frozenset().
The frozenset() returns a new immutable set from an existing one.

'''

skills = {'Problem solving', 'Software design', 'Python programming'}
skills = frozenset(skills)

print(skills)

# To iterate over set using for lopp

for skill in skills:
    print(skill)

# To access the index of current element inside for loop, with default starting index is 0

for index,skill in enumerate(skills):
    print(f'Index is {index} and skill is {skill}')

# To access the index of current element inside for loop, with starting index is 1

for index,skill in enumerate(skills,1):
    print(f'Index is {index} and skill is {skill}')
