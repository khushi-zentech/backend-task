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
    
    for i in range(row+1): # time complexity: O(row^2)
        for j in range(i):
            print(num, end=" ")
            num += 1
        
        print()

# take input from user and validate it
while True:
    # time complexity: depends on how many iterations occur before the break 
    # so, O(row) in worst case and O(1) in best case
    
    row = input("\nEnter number of rows: ")
     
    if row.isdigit():
        # call the function
        print_pattern(int(row))
         
        break
    else:
        print("\nPlease enter a valid positive integer input only.")

# total time complexity: O(row^2) + O(row) = O(row^2)