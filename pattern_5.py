"""
Task - 21: Pattern - 5: Inverted Right Angle Triangle Pattern of Numbers
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""

# define function to print the pattern
def print_pattern(row):
    for i in range(row, 0, -1):
        num = 1
        
        for j in range(i, 0, -1):
            print(num, end=" ")
            num += 1
        print()

# take input from user
row = int(input("Enter number of rows: "))

# call the function
print_pattern(row)