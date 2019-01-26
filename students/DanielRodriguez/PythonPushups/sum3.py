# ----------------------------------------------------------------#
# Title: Push ups
# Change Log: (Who, When, What)
# D.Rodriguez, 2019-01-13, New file
# ----------------------------------------------------------------#

# Given an array of ints length 3, return the sum of all the elements.
#
# sum3([1, 2, 3]) → 6
# sum3([5, 11, 2]) → 18
# sum3([7, 0, 0]) → 7


def sum3(nums):
    # return nums[0]+nums[1]+nums[2]
    # or...
    my_sum = 0
    for x in nums:
        my_sum = my_sum + x

    return my_sum


print(sum3([5, 11, 2]))
