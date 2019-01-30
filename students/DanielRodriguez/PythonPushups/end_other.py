# -------------------------------------------------------------------------------------------------------------------- #
# Title: End Other
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-01-29, Initial release
# -------------------------------------------------------------------------------------------------------------------- #
# Given two strings, return True if either of the strings appears at
# the very end of the other string, ignoring upper/lower case differences
# (in other words, the computation should not be "case sensitive").
# Note: s.lower() returns the lowercase version of a string.
# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True

# -- Data -- #
# declare variables and constants


# -- Processing -- #
def end_other(a, b):
    a = a.lower()
    b = b.lower()
    if a.endswith(b) or b.endswith(a):
        return True
    return False

# -- Presentation (Input/Output) -- #
print(end_other('AbC', 'HiaBc'))
