# ----------------------------------------------------------------#
# Title:
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-01-19, Revision notes
# ----------------------------------------------------------------#
# Given an array of ints, return a new array length 2 containing the
# first and last elements from the original array. The original
# array will be length 1 or more.
#
# make_ends([1, 2, 3]) → [1, 3]
# make_ends([1, 2, 3, 4]) → [1, 4]
# make_ends([7, 4, 6, 2]) → [7, 2]

# -- Data --#
# declare variables and constants


def make_ends(nums):
    # -- Processing --#
    return [nums[0], nums[len(nums)-1]]


# -- Presentation (Input/Output) --#
print(make_ends([1, 2, 3, 4]) )