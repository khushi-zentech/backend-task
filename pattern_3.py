"""
Task - 19: Pattern - 3: Right Angle Triangle Pattern of Alphabets
A
B B
C C C
D D D D
E E E E E
"""

# define function to print the pattern
def print_pattern(row):
    ch = 65
    
    for i in range(row):
        for j in range(i+1):
            print(chr(ch), end=" ")
        ch += 1
        print()

# take input from user
row = int(input("Enter number of rows: "))

# call the function
print_pattern(row)