colors = ['Blue','Red','Green','Orange','Grey']


# 1) for loop to iterate over a list
for color in colors:
    print(f'Color is {color}')


# 2) for loop to iterate over a list with index


for color in enumerate(colors):
    print(f'Color is {color}')



for index,color in enumerate(colors):
    print(f'Index is {index} and Color is {color}')
