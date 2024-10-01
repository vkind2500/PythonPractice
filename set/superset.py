numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}

# Find superset using issuperset method

print(f'set.issuperset(scores,numbers) -> {set.issuperset(numbers,scores)}')

# or

print(f'scores.issuperset(numbers) -> {numbers.issuperset(scores)}')

# Using operator '>='

print(f'Super set using operator \'>=\' -> {numbers>=scores}')

print(f'Super set using operator \'>=\' -> {numbers>=numbers}') # will be true

print(f'Proper super set using operator \'>\' -> {numbers > scores}') # will be true


print(f'Proper super set using operator \'>\' -> {numbers > numbers}') # will be false


