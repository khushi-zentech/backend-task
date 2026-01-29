"""
Task - 3: Implement Circular Queue.
You script should contain four functions.
1. Front: Get the front item from queue
2. Rear: Get the last item from queue
3. enqueue(value)
4. dequeue()
User will be given choice to perform action from above four.
Script should be kept running until user chooses to exit.
"""

# initialize circular queue variables
front = -1
rear = -1

queue_size = int(input("Enter size of Queue: "))
queue = [None] * queue_size


# define front operation to get front item from queue
def get_front():
    if front == -1:
        print("\nQueue is Empty.")
        return
        
    return queue[front]

# define rear operation to get last item from queue
def get_rear():
    if rear == -1:
        print("\nQueue is Empty.")
        return
    
    return queue[rear]

# define enqueue operation to add item to queue
def enqueue(item):
    global front, rear, queue, queue_size

    if (rear+1) % queue_size == front:
        print(f"\nQueue is Full.\nCurrent Queue: {queue}")
        return
    elif front == -1:
        front = 0
        rear = 0
    else:
        rear = (rear+1) % queue_size

    queue[rear] = item
    print(f"\nEnqueue item to Queue: {item}\nCurrent Queue: {queue}")

# define dequeue operation to remove item from queue
def dequeue():
    global front, rear, queue, queue_size

    if front == -1:
        print("\nQueue is Empty.\nNo item to dequeue from Queue.")
        return
    
    item = queue[front]
    queue[front] = None
    
    print(f"\nDequeue item from Queue: {item}\nCurrent Queue: {queue}")
    
    if front == rear:
        front = -1
        rear = -1
    else:
        front = (front + 1) % queue_size

# define menu to interact with user
def menu():
    while True:
        print("\nSelect an Operation to perform on Queue:\n")
        print("1. Front")
        print("2. Rear")
        print("3. Enqueue")
        print("4. Dequeue")
        print("5. Exit")
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            print(f"\nFront at item: {get_front()}, Front: {front}\nCurrent Queue: {queue}")
        elif choice == '2':
            print(f"\nRear at item: {get_rear()}, Rear: {rear}\nCurrent Queue: {queue}")
        elif choice == '3':
            item = input("\nEnter item to enqueue on Queue: ")
            enqueue(item)
        elif choice == '4':
            dequeue()
        elif choice == '5':
            print("\nYou selected to exit.\nThank you!")
            break
        else:
            print("\nInvalid choice.\nPlease Enter a valid choice (1-5).")  
            
# start the menu
menu()