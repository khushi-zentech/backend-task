"""
Task - 8: Matrix Multiplication.
1. Take two 3x3 matrix.
2. take user inputs to fill it up.
3. Multiply them both and store it in another 3x3 matrix.
4. Display the result.
"""

# define function to get matrix input from user
def get_matrix_input():
    matrix = []
    
    for i in range(3):
        row = []
        
        for j in range(3):
            element = int(input(f"Enter Element at [{i}][{j}]: "))
            row.append(element)
        
        matrix.append(row)
    
    return matrix

# define function to multiply two matrix
def matrix_multiplication(matrix_1, matrix_2):
    result_matrix = [[0,0,0], [0,0,0], [0,0,0]]

    for i in range(3):
        for j in range(3):
            for k in range(3):
                result_matrix[i][j] += matrix_1[i][k] * matrix_2[k][j]

    return result_matrix

# display and get user input for matrix_1
print(f"\nEnter the elements for (3x3) Matrix_1:\n")
matrix_1 = get_matrix_input()

# display and get user input for matrix_2
print(f"\nEnter the elements for (3x3) Matrix_2:\n")
matrix_2 = get_matrix_input()

# display the result of multiplication
print(f"\nMatrix_1: {matrix_1}")
print(f"\nMatrix_2: {matrix_2}")

result_matrix = matrix_multiplication(matrix_1, matrix_2)
print(f"\nMultiplication of Matrix: {result_matrix}")