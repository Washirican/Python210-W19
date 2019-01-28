# ---------------------------------------------------------------- #
# Title: Slicing Lab
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-01-27, Initial release
# ---------------------------------------------------------------- #


# -- Processing -- #
def exchange_first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[:1]


def remove_every_other(seq):
    return seq[::2]


def remove_first_last_4(seq):
    return seq[4:-4]


def revers_elements(seq):
    return seq[::-1]


def exchange_thirds(seq):
    # print(len(seq)//3)
    #     last third           first third and middle third
    return seq[-len(seq)//3:] + seq[:-len(seq)//3]
    
    
# -- Data -- #
a_string = "this is a string"
another_string = 'Get the basics of sequence slicing down'
a_tuple = (2, 54, 13, 12, 5, 32)
another_tuple = (2, 54, 13, 12, 5, 32, 88, 37, 55, 2, 97)


# -- Presentation (Input/Output) -- #
# -- With the first and last items exchanged.
assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

# -- With every other item removed.
assert remove_every_other(a_string) == "ti sasrn"
assert remove_every_other(a_tuple) == (2, 13, 5)

# -- With the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
# print(another_string)
# print(remove_first_last_4(another_string))
assert remove_first_last_4(another_string) == 'the basics of sequence slicing '
assert remove_first_last_4(another_tuple) == (5, 32, 88)

# -- With the elements reversed (just with slicing).
# print(a_tuple)
# print(revers_elements(a_tuple))
assert revers_elements(a_string) == "gnirts a si siht"
assert revers_elements(a_tuple) == (32, 5, 12, 13, 54, 2)

# -- With the last third, then first third, then the middle third in the new order.
# print(a_tuple)
# print((5, 32, 2, 54, 13, 12))
# print(exchange_thirds(a_tuple))
# print(exchange_thirds(a_string))
assert exchange_thirds(a_string) == "stringthis is a "
assert exchange_thirds(a_tuple) == (5, 32, 2, 54, 13, 12)



