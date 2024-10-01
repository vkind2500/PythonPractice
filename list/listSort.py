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
















