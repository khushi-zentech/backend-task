"""
Task - 4: Selection sort.
Use a static list.
Use selection sort to sort this list.
"""

# define the selection sort function
def selection_sort(static_list):
    length = len(static_list)

    for i in range(length):
        min_item = i

        print(f"Step - {i+1} :-\n{static_list}")
        for j in range(i+1, length):
            if static_list[j] < static_list[min_item]:
                min_item = j

        print(f"Minimum Element :- {static_list[min_item]}\n")
        static_list[i], static_list[min_item] = static_list[min_item], static_list[i]
        
    return static_list
        
# define a static list
static_list = [23,30,6,12,17,20,1]

# call the selection_sort function
print(f"Sorted List: {selection_sort(static_list)}")