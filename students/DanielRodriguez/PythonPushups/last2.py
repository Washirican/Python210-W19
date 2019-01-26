# ----------------------------------------------------------------#
# Title: Push ups
# Change Log: (Who, When, What)
# D.Rodriguez, 2019-01-19, New file
# ----------------------------------------------------------------#
# Given a string, return the count of the number of times that a
# substring length 2 appears in the string and also as the last 2
# chars of the string, so "hixxxhi" yields 1 (we won't count the
# end substring).

# last2('hixxhi') → 1
# last2('xaxxaxaxx') → 1
# last2('axxxaaxx') → 2

# TODO: Don't understand requirements

def last2(str):
    str_count: int = 0
    for x in range(len(str)):
        print(str[x:x+2], str.count(str[x:x+2]))
        if len(str[x:x + 2]) == 2 and str.count(str[x:x + 2]) > str_count:
            str_count = str.count(str[x:x+2])

    return str_count

# print(last2('hixxhi'))
print(last2('xaxxaxaxx'))
# print(last2('axxxaaxx'))

