# ----------------------------------------------------------------#
# Title: String Formatting Exercise Task 3
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-01-26, Initial release
# ----------------------------------------------------------------#


# -- Processing --#
def format_string(numbers):
    form_string = ''
    for x in range(len(numbers)-1):
        form_string += '{:d}, '
    form_string += '{:d}'
    return len(numbers), form_string.format(*numbers)


# -- Data --#
tplNumbers = (2, 1, 10, 212, 754, 567)


# -- Presentation (Input/Output) --#
intNumCount, strNumbers = format_string(tplNumbers)
print('The ', intNumCount, ' formatted numbers are: ', strNumbers, sep='')
