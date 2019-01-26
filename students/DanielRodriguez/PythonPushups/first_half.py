# ----------------------------------------------------------------#
# Title: Push ups
# Change Log: (Who, When, What)
# D.Rodriguez, 2019-01-18, New file
# ----------------------------------------------------------------#

# Given a string of even length, return the first half. So the
# string "WooHoo" yields "Woo".

# first_half('WooHoo') → 'Woo'
# first_half('HelloThere') → 'Hello'
# first_half('abcdef') → 'abc'

def first_half(str):
    print(str[:len(str)//2])


print(first_half('HelloThere'))