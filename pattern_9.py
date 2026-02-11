"""
Task - 25: Pattern - 9: Pattern of Pascal's Triangle
      1
     1 1
    1 2 1
   1 3 3 1
  1 4 6 4 1
1 5 10 10 5 1
"""

# define a function to print Pascal's Triangle Pattern
def print_pascal_triangle(row):
    for i in range(row+1):
        for j in range(row-i):
            print("", end=" ")
        
        num = 1
        
        for j in range(i+1):
            print(num, end=" ")
            num = num * (i - j) // (j + 1)
        
        print()

# take input from user
row = int(input("Enter the number of rows: "))

# call the function
print_pascal_triangle(row)