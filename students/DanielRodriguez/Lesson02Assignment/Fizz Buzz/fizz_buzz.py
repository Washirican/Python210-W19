# ----------------------------------------------------------------#
# Title: Fizz Buzz
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-01-21, Revision notes
# ----------------------------------------------------------------#

# -- Processing --#
for x in range(1, 101):
    outStr = ""
    if x % 3 == 0:
        outStr = outStr + "Fizz"
    if x % 5 == 0:
        outStr = outStr + "Buzz"
    print(x, outStr)
