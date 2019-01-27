# ---------------------------------------------------------------- #
# Title: String Formatting Exercise Task 5
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-01-26, Initial release
# ---------------------------------------------------------------- #


# -- Data -- #
lstData = ['oranges', 1.3, 'lemons', 1.1]


# -- Processing -- #
fruit1 = lstData[0].upper()
weight1 = lstData[1] * 1.2
fruit2 = lstData[2].upper()
weight2 = lstData[3] * 1.2


strData = f'The weight of an {fruit1[:len(lstData[0])-1]} is {weight1} and the weight of a {fruit2[:len(lstData[2])-1]} is {weight2}'


# -- Presentation (Input/Output) -- #
print(strData)
