# ---------------------------------------------------------------- #
# Title: Cat Dog Push up
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-01-28, Initial release
# ---------------------------------------------------------------- #
# Return True if the string "cat" and "dog" appear the same number of times in the given string.
# cat_dog('catdog') → True
# cat_dog('catcat') → False
# cat_dog('1cat1cadodog') → True


# -- Data -- #
# declare variables and constants
# -- Processing -- #
def cat_dog(str):
    return str.count('cat') == str.count('dog')


# -- Presentation (Input/Output) -- #
print(cat_dog('1cat1cadodog'))