"""
Task - 28: Pattern - 12: Pattern of Diamond
"""

# define function to print Diamond Pattern
def print_diamond_pattern(row):
    for i in range(row):
        for j in range(row-i-1):
            print(" ", end=" ")
        for k in range(2*i+1):
            print("*", end=" ")
        print()

    for i in range(row-2, -1, -1):
        for j in range(row-i-1):
            print(" ", end=" ")
        for k in range(2*i+1):
            print("*", end=" ")
        print()

# take input from user
row = int(input("Enter the number of rows: "))

# call the function
print_diamond_pattern(row)