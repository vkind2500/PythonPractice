from random import randint

'''
    Simple Python while statement example
'''

counter = 0
max = 5

while counter < max:
    print(counter,end=', ')
    counter+=1

print('')

''' 

    Using the while statement to build a simple command prompt program

'''

prompt=''

while prompt!='quit':
    prompt = input('>')
    print(f'Echo : {prompt}')


# while else

'''

    while condition:
        # code block to run
    else:
        # else clause code block

'''

'''

    Suppose that we have the following list of fruits where each fruit is a dictionary that consists of the fruit name and qty keys:
    
    basket = [
        {'fruit': 'apple', 'qty': 20},
        {'fruit': 'banana', 'qty': 30},
        {'fruit': 'orange', 'qty': 10}
    ]
    
    We want to make a program that allows the users to enter a fruit name. Based on the input name, we’ll search for it from the basket list and show its quantity if the fruit is on the list.
    
    In case the fruit is not found, we’ll allow users to enter the quantity for that fruit and add it to the list.

'''


basket = [
        {'fruit': 'apple', 'qty': 20},
        {'fruit': 'banana', 'qty': 30},
        {'fruit': 'orange', 'qty': 10}
    ]

index = 0

fruit_name=input('Enter fruit name:')

while index < len(basket):
    if fruit_name == basket[index]['fruit']:
        print(basket[index]['qty'])
    index+=1
    break
else:
    qty = input('Enter quantity:')
    basket.append({'fruit':fruit_name,'qty':qty})


print(basket)

# Emulating do...while

'''
Unfortunately, Python doesn’t support the do...while loop.
However, we can use the while loop and a break statement to emulate the do...while loop statement.

while True:
    # code block

    # break out of the loop
    if condition
        break
'''

'''

Suppose that we need to develop a number guessing game with the following logic:

First, generate a random number within a range e.g., 0 to 10.
Then, repeatedly prompt users for entering a number.
If the entered number is lower or higher than the random number, give users a hint.
If the entered number equals the random number, the loop stops.


'''

MIN = 0
MAX = 10

# generate secret number
secret_number = randint(MIN,MAX)
attempt = 0

while True:
    input_number = int(input(f'Guess the number between {MIN} and {MAX}: '))
    attempt+=1

    if input_number == secret_number:
        print(f'Bingo! {attempt} attempt(s)')
        break
    elif input_number < secret_number:
        print('It should be bigger.')
    else:
        print('It should be smaller.')

