"""
Task - 26: Pattern - 10: Right Angle Triangle Pattern of Consecutive Numbers
1
2 3
4 5 6
7 8 9 10
"""

# define function to print the pattern
def print_pattern(row):
    num = 1
    
    for i in range(row+1):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()

# take input from user
row = int(input("Enter number of rows: "))

# call the function
print_pattern(row)