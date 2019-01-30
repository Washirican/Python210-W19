# ---------------------------------------------------------------- #
# Title: Count Hi Push up
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-01-28, Initial release
# ---------------------------------------------------------------- #
# Return the number of times that the string "hi" appears anywhere in the given string.
# count_hi('abc hi ho') → 1
# count_hi('ABChi hi') → 2
# count_hi('hihi') → 2

# -- Data -- #
# declare variables and constants

# -- Processing -- #
def count_hi(str):
    return str.count('hi')


# -- Presentation (Input/Output) -- #
print(count_hi('ABChi hi'))
