from functools import wraps

def my_decorator(func):
    @wraps(func)  # This preserves the metadata of func
    def wrapper(*args, **kwargs):
        print("Before the function call.")
        result = func(*args, **kwargs)
        print("After the function call.")
        return result
    return wrapper

@my_decorator
def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

# Calling the decorated function
print(greet("Alice"))

# Checking the name and docstring of the decorated function
print(greet.__name__)  # Outputs: greet
print(greet.__doc__)   # Outputs: Return a greeting message.
help(greet)