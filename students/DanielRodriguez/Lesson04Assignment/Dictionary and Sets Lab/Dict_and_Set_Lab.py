# -------------------------------------------------------------------------------------------------------------------- #
# Title: LAB 4-1: Dictionary and Set Lab
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-01-31, Initial Release
# -------------------------------------------------------------------------------------------------------------------- #

# Create a dictionary containing 'name', 'city', and 'cake' for 'Chris' from 'Seattle' who likes 'Chocolate'
# (so the keys should be: 'name', etc, and values: 'Chris', etc.)
# Display the dictionary.
dicData = {'Name': 'Chris', 'City': 'Seattle', 'Cake': 'Chocolate'}
print(dicData)


# Delete the entry for 'cake'.
# Display the dictionary.
dicData.pop('Cake')
print(dicData)


# Add an entry for 'fruit' with 'Mango' and display the dictionary.
dicData['Fruit'] = 'Mango'
print(dicData)


# Display the dictionary keys.
print(dicData.keys())


# Display the dictionary values.
print(dicData.values())


# Display whether or not 'cake' is a key in the dictionary (i.e. False) (now).
print(True if 'Cake' in dicData.keys() else False)


# Display whether or not 'Mango' is a value in the dictionary (i.e. True).
print(True if 'Mango' in dicData.values() else False)


# Using the dictionary from item 1:
# Make a dictionary using the same keys but with the number of 't's in each value
# as the value (consider upper and lower case?).
dicData2 = {'Name': 'Chris', 'City': 'Seattle', 'Cake': 'Chocolate'}
print(dicData2)


for key, value in dicData2.items():
    # print key, '=', value
    # print type(value)
    dicData2[key] = value.lower().count('t')


print(dicData2)
