#!/usr/bin/env python3
# ---------------------------------------------------------------- #
# Title: List Lab Series 1 to 4
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-01-27, Initial Release notes
# ---------------------------------------------------------------- #

# -- Series 1
# Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
# Display the list (plain old print() is fine…).
lstFruit = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(lstFruit)

# Ask the user for another fruit and add it to the end of the list.
# Display the list.
'''
moreFruit = input('Another fruit?: ')
lstFruit.append(moreFruit.title())
print(lstFruit)
'''
# Ask the user for a number and display the number back to the user and the fruit corresponding to
# that number (on a 1-is-first basis).
'''
response = input('To display fruit name enter a number from 1 to ' + str(len(lstFruit)) + ': ')
print(lstFruit[int(response)-1])
'''
# Add another fruit to the beginning of the list using “+” and display the list.
'''
lstFruit = ['Pineapple'] + lstFruit
print(lstFruit)
'''
# Add another fruit to the beginning of the list using insert() and display the list.
'''
lstFruit.insert(0, 'Banana')
print(lstFruit)
'''
# Display all the fruits that begin with “P”, using a for loop.
'''
print('Fruit that starts with "P":')
for f in lstFruit:
    if f.startswith('P'):
        print(f)
'''
# -- Series 2
# Display the list.
'''
print(lstFruit)
'''
# Remove the last fruit from the list.
# Display the list.
'''
lstFruit.pop(len(lstFruit)-1)
print(lstFruit)
'''
# Ask the user for a fruit to delete, find it and delete it.
'''
lessFruit = input('Type a fruit to delete from the following list: ' + str(lstFruit) + '\n')
lstFruit.remove(lessFruit.title())
print(lstFruit)
'''
# (Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
'''
lstFruit *= 2
print(lstFruit)

lessFruit = input('Type a fruit to delete from the following list: ' + str(lstFruit) + '\n')

while lstFruit.count(lessFruit.title()) > 0:
    lstFruit.remove(lessFruit.title())

print(lstFruit)
'''
# -- Series 3
# Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list
# (making the fruit all lowercase).
# For each “no”, delete that fruit from the list.
# For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values
# (a while loop is good here)
# Display the list.
'''
response = ''
lstFruit2 = lstFruit.copy()
for fruit in lstFruit2:
    while response != 'yes' and response != 'no':
        response = input('Do you like ' + fruit.lower() + '? Yes or No? ')
    if response.lower() == 'no':
        lstFruit.remove(fruit)
        response = ''
    else:
        response = ''
       
print('Fruit you like: ' + str(lstFruit))
'''
# -- Series 4
# Make a new list with the contents of the original, but with all the letters in each item reversed.
# Delete the last item of the original list. Display the original list and the copy.

lstFruitNew = []
for x in lstFruit:
    lstFruitNew.append(x[::-1])

lstFruit.pop(len(lstFruit)-1)
print(lstFruit)
print(lstFruitNew)
    

































