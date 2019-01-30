# ---------------------------------------------------------------- #
# Title: Double Character Push up
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-01-28, Initial release
# ---------------------------------------------------------------- #
# Given a string, return a string where for every char in the original, there are two chars.
# double_char('The') → 'TThhee'
# double_char('AAbb') → 'AAAAbbbb'
# double_char('Hi-There') → 'HHii--TThheerree'


# -- Data -- #
# declare variables and constants
# -- Processing -- #
def double_char(str):
    strNew = ''
    for char in str:
        strNew += char * 2
    return strNew


# -- Presentation (Input/Output) -- #
# AAbb, Hi-There
strData = 'The'
print(double_char(strData)) # == 'TThhee')
