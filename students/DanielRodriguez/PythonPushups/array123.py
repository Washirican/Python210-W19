#----------------------------------------------------------------#
# Title: Explore Errors
# Change Log: (Who, When, What)
# D.Rodriguez, 2019-01-13, New file 
#----------------------------------------------------------------#

# Given an array of ints, return True if the sequence of 
# numbers 1, 2, 3 appears in the array somewhere.
# array123([1, 1, 2, 3, 1]) → True
# array123([1, 1, 2, 4, 1]) → False
# array123([1, 1, 2, 1, 2, 3]) → True


def array123(nums):
    # myString = ''.join(str(e) for e in nums)
    # return myString.count("123") > 0
    return ''.join(str(e) for e in nums).count("123") > 0


   
print(array123([1, 1, 2, 3, 1]))