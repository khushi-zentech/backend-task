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
    for i in range(row, 0, -1): # time complexity: O(row^2)
        num = 1
        
        for j in range(i, 0, -1):
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