'''
Iterable
    * An iterable is an object that can be iterated over.
    * An iterable is an object that includes zero, one, or many elements.
    * range() function is an iterable because we can iterate over its result.
    * Also, a string is an iterable because we can use a for loop to iterate over it.
    * Lists and tuples are also iterables because we can loop over them.

Iterator
    * It is the agent that performs the iteration.
'''

# To get an iterator of iterable object, using iter() function



Students = ['Ram','Shyam','GhanShyam','RadheShyam']
students_iterator = iter(Students)

# Every time, we call the next() function, it returns the next element in the iterable.
# If there isn’t any more element and you call the next() function, you’ll get an exception.

print(next(students_iterator))
print(next(students_iterator))
print(next(students_iterator))
print(next(students_iterator))


# Since we can iterate over an iterator, the iterator is also an iterable object.


students_iterator1 = iter(Students)

for color in students_iterator1:
    print(color)




