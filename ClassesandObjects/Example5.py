class Counter:
    def __init__(self):
        self.__current = 0

    def increment(self):
        self.__current += 1

    def value(self):
        return self.__current

    def reset(self):
        self.__current = 0


counter = Counter()

try:
    print(counter._Counter__current)
    print(counter.__current) 
except AttributeError:
    print(f'AttributeError: \'Counter\' object has no attribute \'__Counter__current\'')
    
    



