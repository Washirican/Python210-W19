# ----------------------------------------------------------------#
# Title: String Formatting Exercise Task 1
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-01-26, Initial release
# ----------------------------------------------------------------#


# -- Data --#
tplData = (2, 123.4567, 10000, 12345.67)


# -- Processing --#
strDataFormat = ("file_{0}{1}{2}{3}".format(
    "{:0>3d} :   ".format(tplData[0]),
    "{:.2f}".format(tplData[1]),
    ", {:.2e}".format(tplData[2]),
    ", {:.3e}".format(tplData[3])))


# -- Presentation (Input/Output) --#
print(strDataFormat)

