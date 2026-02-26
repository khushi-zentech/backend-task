"""
Task - 27: Pattern - 11: Pattern of Spiral number
1 2 3 4
12 13 14 5
11 16 15 6
10 9 8 7
"""

# define function to print spiral number pattern
def print_pattern(row):
    num = 1
    spiral_matrix = [[0] * row for i in range(row)]
    
    for i in range((row+1) // 2): # time complexity: O(row^2)
        for j in range(i, row - i):
            spiral_matrix[i][j] = num
            num += 1
        
        for j in range(i+1, row-i):
            spiral_matrix[j][row-i-1] = num
            num += 1
        
        for j in range(row-i-2, i-1, -1):
            spiral_matrix[row-i-1][j] = num
            num += 1
        
        for j in range(row-i-2, i, -1):
            spiral_matrix[j][i] = num
            num += 1
    
    for i in range(row): # time complexity: O(row^2)
        for j in range(row):
            print(spiral_matrix[i][j], end=" ")
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

# total time complexity: O(row^2) + O(row^2) + O(row) = O(row^2)