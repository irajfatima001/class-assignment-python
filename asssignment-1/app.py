#-----------------pyramid---------------------
# Take input for the number of rows in the pyramid
rows = int(input("Enter the number of rows: "))

# Loop through each row
for i in range(1, rows + 1):
    # Print spaces to center the pyramid
    print(" " * (rows - i), end="")
    
    # Print '*' with repetition
    print("*" * (2 * i - 1))

