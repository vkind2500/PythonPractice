def times(n):
    return lambda x:n*x

double = times(3)
print(double(2))