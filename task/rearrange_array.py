"""
Task - 16: Rearrange array such that A[A[i]] is set i for every element A[i].

Input: [1, 3, 4, 2, 0]
Output: [4, 0, 3, 1, 2]

Explanation:
A[0] = 1, A[1] becomes 0
A[1] = 3, A[3] becomes 1
A[2] = 4, A[4] becomes 2
A[3] = 2, A[2] becomes 3
A[4] = 0, A[0] becomes 4
"""

# define function to rearrange array
def rearrange_array(input_list):
    output_list = [0 for i in range(len(input_list))]

    for i in range(0, len(input_list)):
        element = input_list[i]
        output_list[element] = i
    
    return output_list

# take static input list
input_list = [1, 3, 4, 2, 0]

# display output
print(f"\nInput List: {input_list}")
print(f"\nRearranged Output List: {rearrange_array(input_list)}")