#----------------------------------------------------------------#
# Title: Pushups
# Change Log: (Who, When, What)
# D.Rodriguez, 2019-01-13, New file 
#----------------------------------------------------------------#
# Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
# string_bits('Hello') → 'Hlo'
# string_bits('Hi') → 'H'
# string_bits('Heeololeo') → 'Hello'

def string_bits(str):
    myList = list(str)
    myString = ""
    for x in range(0, len(myList),2):
        myString=myString+(myList[x])
    return myString

print(string_bits('Hello'))
print(string_bits('Hi'))
print(string_bits('Heeololeo'))