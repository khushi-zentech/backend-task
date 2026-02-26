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
    for i in range(1, row+1): # time complexity: O(row^2)
        for j in range(row-i):
            print(" ", end=" ")
        
        num = i
        
        for k in range(2*i-1): 
            print(num, end=" ")
            
            if k < i-1:
                num += 1
            else:
                num -= 1
        
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