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
    for i in range(row+1): # time complexity: O(row^2)
        for j in range(row-i):
            print("", end=" ")
        
        num = 1
        
        for k in range(i+1):
            print(num, end=" ")
            num = num * (i - k) // (k + 1)
        
        print()

# take input from user and validate it
while True:
    # time complexity: depends on how many iterations occur before the break 
    # so, O(row) in worst case and O(1) in best case
    
    row = input("\nEnter number of rows: ")
        
    if row.isdigit():      
        # call the function
        print_pascal_triangle(int(row))
             
        break
    else:
        print("\nPlease enter a valid positive integer input only.")

# total time complexity: O(row^2) + O(row) = O(row^2)