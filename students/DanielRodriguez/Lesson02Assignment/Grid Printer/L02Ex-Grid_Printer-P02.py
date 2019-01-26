# ----------------------------------------------------------------#
# Title: Grid Printer 2: Makes 2x2 grid, each cell of n size
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-01-20, Revision notes
# ----------------------------------------------------------------#

# -- Data --#
# None


# -- Processing --#
def print_grid(n):
    print("+", end=" ")
    for col in range(2):
        for x in range(n):
            print("-", end=" ")
        print("+", end=" ")
    print("")
    for row in range(n):
        for x in range(2):
            print("|", " " * (n * 2), end="")
        print("|", end="")
        print("")
    print("+", end=" ")
    for col in range(2):
        for x in range(n):
            print("-", end=" ")
        print("+", end=" ")
    print("")
    for row in range(n):
        for x in range(2):
            print("|", " " * (n * 2), end="")
        print("|", end="")
        print("")
    print("+", end=" ")
    for col in range(2):
        for x in range(n):
            print("-", end=" ")
        print("+", end=" ")
    print(" ")


# -- Presentation (Input/Output) --#
print_grid(3)
