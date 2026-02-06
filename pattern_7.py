"""
Task - 23: Pattern - 7: Pyramid Pattern of Numbers
        1
      2 3 2
    3 4 5 4 3
  4 5 6 7 6 5 4
5 6 7 8 9 8 7 6 5
"""

# define a function to print the pyramid pattern of numbers
def print_pattern(row):
    for i in range(1, row+1):
        for j in range(row-i):
            print(" ", end="")
        
        num = i
        
        for k in range(2*i-1):
            print(num, end=" ")
            
            if k < i-1:
                num += 1
            else:
                num -= 1
        
        print()

# take input from user
row = int(input("Enter the number of rows: "))

# call the function
print_pattern(row)