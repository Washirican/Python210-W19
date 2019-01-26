# ----------------------------------------------------------------#
# Title: Push ups
# Change Log: (Who, When, What)
# D.Rodriguez, 2019-01-18, New file
# ----------------------------------------------------------------#

# Given a string, return a new string made of 3 copies of the last 2
# chars of the original string. The string length will be at least 2.
#
# extra_end('Hello') → 'lololo'
# extra_end('ab') → 'ababab'
# extra_end('Hi') → 'HiHiHi'


def extra_end(str):
    # mylist = list(str)
    # return "".join(mylist[len(mylist) - 2:len(mylist)]) * 3

    return str[len(str)-2:len(str)] *3


print(extra_end('Hello'))


