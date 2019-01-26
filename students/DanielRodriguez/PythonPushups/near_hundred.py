#----------------------------------------------------------------#
# Title: Pushups
# Change Log: (Who, When, What)
# D.Rodriguez, 2019-01-13, New file 
#----------------------------------------------------------------#

# Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.
# near_hundred(93) → True
# near_hundred(90) → True
# near_hundred(89) → False

def near_hundred(n):
    if abs(n-100) <= 10 or abs(n-200) <= 10:
        return True
    else:
        return False 
  



print(near_hundred(93))
print(near_hundred(90))
print(near_hundred(89))