# ---------------------------------------------------------------- #
# Title: String Formatting Exercise Task 4
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-01-26, Initial release
# ---------------------------------------------------------------- #


# -- Data -- #
tplNumbers = (4, 30, 2017, 2, 27)


# -- Processing -- #
strNumbers = '{:0>2d} {} {} {:0>2d} {}'.format(tplNumbers[3], tplNumbers[4], tplNumbers[2], tplNumbers[0], tplNumbers[1])


# -- Presentation (Input/Output) -- #
print('Numbers are: ', strNumbers)
