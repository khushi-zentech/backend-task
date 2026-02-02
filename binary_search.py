"""
Task - 7: Binary search.
Use a static list.
Use Binary search to find element asked by user.
Use one of the sorting algorithm that you have developed to sort list here.
"""

# define the bubble_sort function to sort the static list
def bubble_sort(static_list):
    length = len(static_list)

    for i in range(length):
        if i == length - 1:
            return static_list
        
        for j in range(0, length - i - 1):
            if static_list[j] > static_list[j+1]:
                static_list[j], static_list[j+1] = static_list[j+1], static_list[j]
    
# define the binary_search function to find the key in sorted list 
def binary_search(key, static_list):
    low = 0
    high = len(static_list) - 1

    while low <= high:
        mid = low + (high-low) // 2
        
        if key == static_list[mid]:
            return mid
        elif key > static_list[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# define a static list
static_list = [23,30,6,12,17,20,1]

# call the bubble_sort function
print(f"\nStatic List :- {static_list}")
print(f"\nSorted List :- {bubble_sort(static_list)}")

# take input from user
key = int(input("\nEnter a key to find in Sorted List :- "))

# call the binary_search function
result = binary_search(key, static_list)

# display the result
if result != -1:
    print(f"\n{key} is present at index :- {result}")
else:
    print(f"\n{key} is not present in List.") 