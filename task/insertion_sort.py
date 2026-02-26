"""
Task - 6: Insertion sort.
Use a static list.
Use insertion sort to sort this list.
"""

# define the insertion_sort function
def insertion_sort(static_list):
    for i in range(1, len(static_list)):
        swap_element = static_list[i]
        j = i - 1

        while j >= 0 and swap_element < static_list[j]:
            static_list[j+1] = static_list[j]
            j = j-1
            
        static_list[j+1] = swap_element
        print(f"\nStep - {i} :-\n{static_list}")
        
    return static_list

# define a static list
static_list = [23,30,6,12,17,20,1]

# call the insertion_sort function
print(f"\nSorted List: {insertion_sort(static_list)}")