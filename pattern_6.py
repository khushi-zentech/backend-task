"""
Task - 22: Pattern - 6: Pyramid Pattern of *
         *
       * * *
     * * * * *
   * * * * * * *
 * * * * * * * * *
"""

# define a function to print the pyramid pattern
def print_pattern(row):
    for i in range(1, row+1):
        for j in range(row-i):
            print(" ", end="")
        
        for k in range(2*i-1):
            print("*", end="")
        print()

# take input from user
row = int(input("Enter the number of rows: "))

# call the function
print_pattern(row)