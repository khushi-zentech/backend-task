"""
Task - 5: Bubble sort.
Use a static list.
Use bubble sort to sort this list.    
"""

# define the bubble sort function
def bubble_sort(static_list):
    length = len(static_list)

    for i in range(length):
        if i == length - 1:
            return static_list
        else:
            print(f"\nStep - {i+1}:")
        
        for j in range(0, length - i - 1):
            if static_list[j] > static_list[j+1]:
                static_list[j], static_list[j+1] = static_list[j+1], static_list[j]
            print(static_list)
            
# define a static list
static_list = [23,30,6,12,17,20,1]

# call the bubble_sort function
print(f"\nSorted List: {bubble_sort(static_list)}")