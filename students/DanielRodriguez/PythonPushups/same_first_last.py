# ----------------------------------------------------------------#
# Title: Push ups
# Change Log: (Who, When, What)
# D.Rodriguez, 2019-01-13, New file
# ----------------------------------------------------------------#
#
# Given an array of ints, return True if the array is length 1 or more,
# and the first element and the last element are equal.
#
# same_first_last([1, 2, 3]) → False
# same_first_last([1, 2, 3, 1]) → True
# same_first_last([1, 2, 1]) → True


def same_first_last(nums):
    if len(nums) >= 1:
        if nums[0] == nums[len(nums)-1]:
            return True
        else:
            return False
    else:
        return False


print(same_first_last([]))

