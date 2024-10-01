#1) Using the Python List sort() method to sort a list of strings

guests = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer']

# Sort the elements in the guests alphabetically
guests.sort()
print(guests)

# Sort the elemnts in the guests in reverse alphabetically
guests.sort(reverse = True)
print(guests)

#2) Using the Python List sort() method to sort a list of numbers

scores = [5, 7, 4, 6, 9, 8]

# sort numbers in the scores list from smallest to largest
scores.sort()
print(scores)

# To sort numbers from the largest to smallest
scores.sort(reverse = True)
print(scores)

# 3) Using the Python List sort() method to sort a list of tuples

companies = [('Google', 2019, 134.81),
             ('Apple', 2019, 260.2),
             ('Facebook', 2019, 70.7)]

# Define Sort Key Function

def sort_key(company):
    return company[2]

# sort the companies by revenue in reverse order
companies.sort(key=sort_key,reverse = True)

# show the sorted companies
print(companies)

# Using lambda expression to sort the companies by revenue from low to high:

companies.sort(key = lambda company:company[2])
print(companies)

# Introduction to sorted() function

print()
print('Introduction to sorted() function.........')
print()

# 1) Using Python sorted() function to sort a list of strings

my_guests = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer']

# sorted() function to sort a list of strings in alphabetical order
sorted_guests = sorted(my_guests)

print(f'My_Guests List -> {my_guests}')
print(f'My Sorted Guests List -> {sorted_guests}')

# sorted() function to sort the guests list in the reverse alphabetical order
sorted_guests = sorted(my_guests,reverse=True)
print(f'Reverse Sorted Guests List -> {sorted_guests}')

# 2) Using Python sorted() function to sort a list of numbers

my_scores = [5, 7, 4, 6, 9, 8]

# sort a list of numbers from smallest to largest
sorted_scores = sorted(my_scores)

print(f'My score care -> {my_scores}')
print(f'My sorted score card -> {sorted_scores}')

#It sorts a list of numbers from largest to smallest:
sorted_scores = sorted(my_scores,reverse=True)
print(f'My Reverse sorted score card -> {sorted_scores}')

# 3) Using the Python sorted() method to sort a list of tuples

my_companies = [('Google', 2019, 134.81),
             ('Apple', 2019, 260.2),
             ('Facebook', 2019, 70.7)]

def sort_key(company):
    return company[2]

my_sorted_companies = sorted(my_companies,key=sort_key)
print(f'My sorted companies -> {my_sorted_companies}')

# 4) Using Lambda Expression

my_sorted_companies = sorted(my_companies,key= lambda company:company[2],reverse = True)
print(f'My sorted companies -> {my_sorted_companies}')















