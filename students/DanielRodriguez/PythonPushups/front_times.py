#----------------------------------------------------------------#
# Title: Pushups
# Change Log: (Who, When, What)
# D.Rodriguez, 2019-01-13, New file 
#----------------------------------------------------------------#

# Given a string and a non-negative int n, we'll say that the front of 
# the string is the first 3 chars, or whatever is there if the string is 
# less than length 3. Return n copies of the front;
# front_times('Chocolate', 2) → 'ChoCho'
# front_times('Chocolate', 3) → 'ChoChoCho'
# front_times('Abc', 3) → 'AbcAbcAbc'


def front_times(str, n):
  # print (str)
  myList = list(str)
  # print(myList)
  myString = ""
  for x in myList[:3]:
    myString = myString + x
  return (myString) *n