# ----------------------------------------------------------------#
# Title: Push ups
# Change Log: (Who, When, What)
# D.Rodriguez, 2019-01-18, New file
# ----------------------------------------------------------------#

# Given a string, return a version without the first and last char,
# so "Hello" yields "ell". The string length will be at least 2.
#
# without_end('Hello') → 'ell'
# without_end('java') → 'av'
# without_end('coding') → 'odin'


def without_end(str):
    return str[1:len(str)-1]



print(without_end('java'))