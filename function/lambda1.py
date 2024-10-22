def get_full_name(first_name,last_name,formatter):
    """
    The get_full_name() function accepts three arguments:

    First name (first_name)
    Last name (last_name)
    A function that will format the full name (formatter).

    """
    return formatter(first_name,last_name)


full_name =  get_full_name(
    "John",
    "Doe",
    lambda first_name,last_name:f'{first_name} {last_name}'
) 

print(full_name)

full_name =  get_full_name(
    "Jane",
    "Merry",
    lambda first_name,last_name:f'{last_name} {first_name}'
)

print(full_name)