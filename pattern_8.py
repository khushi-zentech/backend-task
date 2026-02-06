"""
Task - 24: Pattern - 8: Inverted Pyramid Pattern of *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
"""

# define a function to print the inverted pyramid pattern
def print_pattern(row):
    for i in range(row, 0, -1):
        for j in range(row-1, i-1, -1):
            print(" ", end=" ")
        
        for k in range(2*i-1, 0, -1):
            print("*", end=" ")
        print()

# take input from user
row = int(input("Enter the number of rows: "))

# call the function
print_pattern(row)