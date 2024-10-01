numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}

# Find subset using issubset method

print(f'set.issubset(scores,numbers) -> {set.issubset(scores,numbers)}')

# or

print(f'scores.issubset(numbers) -> {scores.issubset(numbers)}')

# Using operator '<='

print(f'Subset using operator \'<=\' -> {scores<=numbers}')

print(f'Subset using operator \'<=\' -> {numbers<=numbers}') # will be true

print(f'Proper Subset using operator \'<=\' -> {scores<numbers}') # will be true

print(f'Proper Subset using operator \'<=\' -> {numbers<numbers}') # will be false






