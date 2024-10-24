# Define a class 'Person' to represent a person with attributes name and age
class Person:
    # Constructor method (__init__) to initialize the name and age attributes
    def __init__(self, name, age):
        self.name = name  # Store the person's name
        self.set_age(age)  # Call the set_age method to assign age (with validation)

    # Method to set the person's age with validation
    def set_age(self, age):
        # Raise a ValueError if the provided age is not positive
        if age <= 0:
            raise ValueError('The age must be positive')
        self._age = age  # Assign age to a private attribute (_age)

    # Method to retrieve the person's age
    def get_age(self):
        return self._age  # Return the value of the private attribute (_age)
    
    # Create a property 'age' that allows getting and setting age using get_age and set_age methods
    age = property(get_age, set_age)
    
# Create an instance of Person with the name 'John' and age 18
john = Person('John', 18)

# Print John's current age
print(f'John age is {john.age}')    

# Change John's age to 57 using the setter method
john.age = 57

# Print John's updated age
print(f'John age is {john.age}')

# Try setting an invalid age (-1) and catch the ValueError exception
try:
    john.age = -1
except ValueError:
    # Print a message indicating that -1 is not a valid age
    print('John age cannot be -1')