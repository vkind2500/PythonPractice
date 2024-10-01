"""

In Python, a partial function is a concept that comes from the functools module.
It allows us to fix a certain number of arguments of a function and generate a new function.
This can be particularly useful when we need to frequently call a function with the same arguments.

"""

''' To create a partial function, we use the functools.partial function. Here's the basic syntax:

from functools import partial

partial_function = partial(original_function, fixed_arg1, fixed_arg2, ...) '''

# Suppose we have a function that multiplies three numbers:

def multiply(x, y, z):
    return x * y * z

# we can create a partial function that always multiplies by 2 and 3:

from functools import partial

multiply_by_2_and_3 = partial(multiply, 2, 3)

# Now, multiply_by_2_and_3 only requires one argument:

result = multiply_by_2_and_3(4)  # This is equivalent to multiply(2, 3, 4)
print(result)  # Output: 24

# Example in a Real-World Scenario
# Imagine we are working with a logging system and we want to create different logging functions for different log levels:

import logging


# Set up the basic configuration for logging
logging.basicConfig(level=logging.DEBUG)

# Create partial functions for different log levels
info_log = partial(logging.log, logging.INFO)
debug_log = partial(logging.log, logging.DEBUG)
error_log = partial(logging.log, logging.ERROR)

# Use the partial functions
info_log("This is an info message")
debug_log("This is a debug message")
error_log("This is an error message")






