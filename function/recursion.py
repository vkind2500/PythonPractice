# Develop a countdown function that counts down from a specified number to zero.

def count_down(n):
    print(n)
    next = n-1
    if next > 0:
        count_down(next)



count_down(6)

# Calculate a sum of a sequence e.g., from 1 to 100.

def sum(n):
    total = 0
    if n > 0 :
        total = n + sum(n-1)
    return total

print(f'Sum of sequence -> {sum(100)}')

# Using Ternary Operator

def sum1(n):
    return n + sum(n-1) if n > 0 else 0


print(f'Sum of sequence -> {sum1(100)}')


