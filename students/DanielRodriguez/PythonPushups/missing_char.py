#----------------------------------------------------------------#
# Title: Pushups
# Change Log: (Who, When, What)
# D.Rodriguez, 2019-01-13, New file 
#----------------------------------------------------------------#

# Given a non-empty string and an int n, return a new string where the char at index n has been removed. 
# The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).
# missing_char('kitten', 1) → 'ktten'
# missing_char('kitten', 0) → 'itten'
# missing_char('kitten', 4) → 'kittn'


def missing_char(str, n):
  str2 = ""
  for x in str.split(str[n],1):
    str2 = str2 + x
  return str2 



  
print(missing_char('kitten', 1))
print(missing_char('kitten', 0))
print(missing_char('kitten', 4) )