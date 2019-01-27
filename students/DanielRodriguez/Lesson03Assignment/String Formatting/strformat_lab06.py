# ---------------------------------------------------------------- #
# Title: String Formatting Exercise Task 5
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-01-26, Initial release
# ---------------------------------------------------------------- #
# -- Data -- #
strRow1 = 'Mark Ruffalo,30,5000'
strRow2 = 'Scarlett Johansson,32,500000'
strRow3 = 'Robert Downey Jr.,89,500'
strRow4 = 'Brie Larson,62,30'


# -- Processing -- #
lstTableData = [strRow1, strRow2, strRow3, strRow4]


# -- Presentation (Input/Output) -- #
strHeader = '{:20}{:10}{:20}'.format('Name', 'Age', 'Net Worth')
print(strHeader)
for x in lstTableData:
    print('{:20}{:10}{:20}'.format(x.split(',')[0], x.split(',')[1], x.split(',')[2]))

