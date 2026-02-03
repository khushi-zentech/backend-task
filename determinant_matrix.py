"""
Task - 9: Find determinant of 3x3 matrix.
"""

# define function to get matrix input from user
def get_matrix_input():
    matrix = []
    
    for i in range(3):
        row = []
        
        for j in range(3):
            element = int(input(f"Enter element at [{i}][{j}]: "))
            row.append(element)
        
        matrix.append(row)
    
    return matrix

# define function to calculate determinant of 3x3 matrix
def calculate_determinant(matrix):
    term_1 = matrix[0][0] * ((matrix[1][1] * matrix[2][2]) - (matrix[1][2] * matrix[2][1]))
    term_2 = matrix[0][1] * ((matrix[1][0] * matrix[2][2]) - (matrix[1][2] * matrix[2][0]))
    term_3 = matrix[0][2] * ((matrix[1][0] * matrix[2][1]) - (matrix[1][1] * matrix[2][0]))
    
    determinant = term_1 - term_2 + term_3
    
    return determinant

# display the results
print("\nEnter elements for 3x3 Matrix:\n")
matrix = get_matrix_input()

print(f"\nYou given matrix: {matrix}")
print(f"\nDeterminant (det(matrix) or |matrix|): {calculate_determinant(matrix)}")