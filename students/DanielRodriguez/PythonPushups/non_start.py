# ----------------------------------------------------------------#
# Title: Push ups
# Change Log: (Who, When, What)
# D.Rodriguez, 2019-01-18, New file
# ----------------------------------------------------------------#

# Given 2 strings, return their concatenation, except omit the first
# char of each. The strings will be at least length 1.
#
# non_start('Hello', 'There') → 'ellohere'
# non_start('java', 'code') → 'avaode'
# non_start('shotl', 'java') → 'hotlava'


def non_start(a, b):
    return a[1:] + b[1:]




print(non_start('Hello', 'There'))