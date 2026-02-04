"""
Task - 2: Implement Queue.
You script should contain three functions
1. enqueue
2. dequeue
3. peek
User will be given choice to perform action from above three.
Script should be kept running until user chooses to exit.
"""

# define enqueue operation to add item to queue
def enqueue(queue, item):
    queue.append(item)
    print(f"\nEnqueue item to Queue: {item}")
    return queue

# define dequeue operation to remove item from queue
def dequeue(queue):
    if queue:
        item = queue.pop(0)
        print(f"\nDequeue item from Queue: {item}")
    else:
        print("\nQueue is Empty.\nNo item to dequeue from Queue.")
    return queue

# define peek operation to view item at front of queue
def peek(queue):
    if queue:
        print(f"\nItem at Front of Queue: {queue[0]}")
    else:
        print("\nQueue is Empty.\nNo item at Front of Queue.")
   
# define menu to interact with user 
def menu():
    queue = []
    while True:
        print("\nSelect an Operation to perform on Queue:\n")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Exit")
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            item = input("\nEnter item to enqueue on Queue: ")
            queue = enqueue(queue, item)
            print(f"\nCurrent Queue: {queue}")
        elif choice == '2':
            queue= dequeue(queue)
            print(f"\nCurrent Queue: {queue}")
        elif choice == '3':
            peek(queue)
        elif choice == '4':
            print("\nYou selected to exit.\nThank you!")
            break
        else:
            print("\nInvalid choice.\nPlease Enter a valid choice (1-4).")  

# start the menu 
menu()