"""
Task - 20: Pattern - 4: Inverted Right Angle Triangle Pattern of *
* * * * *
* * * *
* * *
* *
*
"""

# define function to print the pattern
def print_pattern(row):
    for i in range(row, 0, -1):
        for j in range(i, 0, -1):
            print("*", end=" ")
        print()

# take input from user
row = int(input("Enter number of rows: "))

# call the function
print_pattern(row)