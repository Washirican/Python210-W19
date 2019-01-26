# ----------------------------------------------------------------#
# Title: Push ups
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-01-19, Revision notes
# ----------------------------------------------------------------#
# Given an array of ints, return the sum of the first 2 elements in
# the array. If the array length is less than 2, just sum up the
# elements that exist, returning 0 if the array is length 0.
#
# sum2([1, 2, 3]) → 3
# sum2([1, 1]) → 2
# sum2([1, 1, 1, 1]) → 2

# -- Data --#
# declare variables and constants
# -- Processing --#
# perform tasks
# -- Presentation (Input/Output) --#
# get user input
# send program output


def sum2(nums):
    return sum(nums[:2])


print(sum2([2, 4, 1, 6, 7, 9]))
