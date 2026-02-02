"""
Task - 6: Insertion sort.
Use a static list.
Use insertion sort to sort this list.
"""

# define the insertion_sort function
def insertion_sort(static_list):
    for i in range(1, len(static_list)):
        temp = static_list[i]
        j = i - 1

        while True:
            if temp < static_list[j] and j >= 0:
                static_list[j+1] = static_list[j]
                j = j-1
            else:
                break
            
        static_list[j+1] = temp
        print(f"\nStep - {i} :-\n{static_list}")
        
    return static_list

# define a static list
static_list = [23,30,6,12,17,20,1]

# call the insertion_sort function
print(f"\nSorted List: {insertion_sort(static_list)}")