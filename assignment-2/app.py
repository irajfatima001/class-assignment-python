#----------------------diamond pyramid-----------------------
# Take input for the number of rows (half of the diamond)
rows = int(input("Enter the number of rows: "))

# Upper Pyramid
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

# Lower Inverted Pyramid
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
