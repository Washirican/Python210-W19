# ----------------------------------------------------------------#
# Title: Fibonacci Series
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-01-21, Revision notes
# ----------------------------------------------------------------#


# -- Processing --#
def fibonacci(n):
    """
    :desc    :  This function returns the nth value in the Fibonacci Series (starting with zero index)
    :param  n: Series value to be returned
    :type   n: int
    :return :  Returns the nth value in the series
    :rtype  :   list
    """
    series = [0, 1]
    if n == 0:
        return [0], "Fibonacci Series"
    elif n == 1:
        return series, "Fibonacci Series"
    elif n >= 2:
        for x in range(2, n + 1):
            series.append(series[x - 2] + series[x - 1])
        return series, "Fibonacci Series"


def lucas(n):
    """
    :desc    :  This function returns the nth value in the Lucas Numbers (starting with zero index)
    :param  n: Series value to be returned
    :type   n: int
    :return   :  Returns the nth value in the series
    :rtype    :   list
    """
    series = [1, 2]
    if n == 0:
        return [1], "Lucas Numbers"
    elif n == 1:
        return series, "Lucas Numbers"
    elif n >= 2:
        for x in range(2, n + 1):
            series.append(series[x - 2] + series[x - 1])
        return series, "Lucas Numbers"


def sum_series(n, n0=0, n1=1):
    """
    :desc    :  This function returns the nth value in the Fibonacci Series or
                Lucas Numbers based on optional parameters
    :param  n:  Series value to be returned
    :param  n0: Series default value 0
    :param  n1: Series default value 1
    :type   n:  int
    :type   n0: int
    :type   n1: int
    :return   : Returns the nth value in the series
    :rtype    : list
    """
    if [n0, n1] == [0, 1]:
        return fibonacci(n)
    elif [n0, n1] == [1, 2]:
        return lucas(n)
    else:
        series = [n0, n1]
        if n == 0:
            return [n0], "Custom Series"
        elif n == 1:
            return series, "Custom Series"
        elif n >= 2:
            for x in range(2, n + 1):
                series.append(series[x - 2] + series[x - 1])
            return series, "Custom Series"


n = 2
# series_val, series_name = fibonacci(n)
# series_val, series_name = lucas(n)
series_val, series_name = sum_series(n, 0, 1)


# -- Presentation (Input/Output) --#
print("The nth value in the ", str(series_name), " for n = ", n, " is: ", series_val, sep="")

