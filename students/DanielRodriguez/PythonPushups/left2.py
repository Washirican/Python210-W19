# ----------------------------------------------------------------#
# Title: Push ups
# Change Log: (Who, When, What)
# D.Rodriguez, 2019-01-18, New file
# ----------------------------------------------------------------#

# Given a string, return a "rotated left 2" version where the first 2
# chars are moved to the end. The string length will be at least 2.
#
# left2('Hello') → 'lloHe'
# left2('java') → 'vaja'
# left2('Hi') → 'Hi'


def left2(str):
    return str[2:] + str[:2]


print(left2('java'))