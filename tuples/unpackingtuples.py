# Unpacking a tuple means splitting the tuple’s elements into individual variables.

x,y = (1,2)
print(f'x is {x} and y is {y}')

# swap two numbers using concept of tuples unpacking

x = 10
y = 20

print(f'x = {x} and y = {y}')

x,y = y,x

print(f'x = {x} and y = {y}')

'''

Please note that while unpacking tuples , the no of variables on left side should be equal to number of elements in a tuple.

For example :-

x,y = 10,20,30

or

x,y,z = 10,20

will throw Value Error


'''


# Unpacking using * Operator

x,y,*z = 10,20,30,40

print(f'x is {x}, y is {y} and z is {z}')  # Python packs the remaining elements 100 and 0.5 into a list and assigns it to the other variable.

'''

We can use only 1 * operator on left hand side of expression to unpack rest of elements.
For example :-

x,y,*z,*u = 10,20,30,40,50

will give Syntax Error

'''

# Using * operator on right hand side

odd_number = 1,3,5

even_number = 2,



print((*odd_number,*even_number))
