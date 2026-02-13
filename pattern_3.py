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
    
    for i in range(row): # time complexity: O(row^2)
        for j in range(i+1):
            print(chr(ch), end=" ")
        ch += 1
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