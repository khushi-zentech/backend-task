"""
Task - 1: Implement Stack.
Your script should contain three functions.
1. push
2. pop
3. peep
User will be given choice to perform action from above three.
Script should be kept running until user chooses to exit.
"""

# define push operation to add item at top of stack
def push(stack, item):
    stack.append(item)
    print(f"\nPushed item to stack: {item}")
    return stack

# define pop operation to remove top item from stack
def pop(stack):
    if len(stack):
        item = stack.pop()
        print(f"\nPopped item from stack: {item}")
    else:
        print("\nStack is empty.\nNo item to pop on Stack.")
    return stack

# define peep operation to view top item of stack
def peep(stack):
    if len(stack):
        item = stack[-1]
        print(f"\nItem at Top: {item}")
    else:
        print("\nStack is empty.\nNo item at Top of Stack.")
        
# define menu to interact with user
def menu():
    stack = []
    while True:
        print("\nSelect an Operation to perform on Stack:\n")
        print("1. Push")
        print("2. Pop")
        print("3. Peep")
        print("4. Exit")
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            item = input("\nEnter item to push on Stack: ")
            stack = push(stack, item)
            print(f"\nCurrent Stack: {stack}")
        elif choice == '2':
            stack = pop(stack)
            print(f"\nCurrent Stack: {stack}")
        elif choice == '3':
            peep(stack)
        elif choice == '4':
            print("\nYou selected to exit.\nThank you!")
            break
        else:
            print("\nInvalid choice.\nPlease Enter a valid choice (1-4).")  
            
# start the menu
menu()