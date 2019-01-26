# ----------------------------------------------------------------#
# Title: Grid Printer 3: Makes row x col grid, each cell of n size
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-01-21, Revision notes
# ----------------------------------------------------------------#


# -- Processing --#
def print_row_header(col, n):
    # Column Header
    print("+", end=" ")
    for col in range(col):
        for x in range(n):
            print("-", end=" ")
        print("+", end=" ")
    print("")


def print_row(col, n):
    # Rows
    for row in range(n):
        for x in range(col):
            print("|", " " * (n * 2), end="")
        print("|", end="")
        print("")
    print("", end="")


def print_grid(row, col, n):
    print_row_header(col, n)
    for x in range(row):
        print_row(col, n)
        print_row_header(col, n)


# -- Data --#
row = int(input("Enter number of rows: "))
col = int(input("Enter number of columns: "))
n = int(input("Enter size of cells: "))


# -- Presentation (Input/Output) --#
print_grid(row, col, n)
