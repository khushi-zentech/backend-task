"""
Task - 18: Pattern - 2: Right Angle Triangle Pattern of Numbers
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

# define function to print the pattern
def print_pattern(row):
    for i in range(row+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()

# take input from user
row = int(input("Enter number of rows: "))

# call the function
print_pattern(row)