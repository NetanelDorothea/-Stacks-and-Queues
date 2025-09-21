# Import the Node class you created in node.py
from node import Node

# Implement your Queue class here
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        """Adds a new item to the end of the line"""
        new_node = Node(value)
        if not self.front:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        """Removes and returns the item at the front of the line."""
        if not self.front:
            return None
        removed_node = self.front
        self.front = self.front.next
        # If this was the last node removed, then rear should be updated as well 
        if not self.front:
            self.rear = None 
        return removed_node.value
    
    def peek(self):
        """Returns the item at the front of the line without removing it"""
        if self.front:
            return self.front.value
        else:
            return None
        
    def print_queue(self):
        """Prints all values in order starting at the front and working towards the rear."""
        current = self.front
        if not current:
            print("Queue is empty")
            return
        while current:
            print(f"- {current.value}")
            current = current.next # Update current to next value
    


def run_help_desk():
    qu = Queue()
    

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            qu.enqueue(name) # Add the customer to the queue
            print(f"{name} added to the queue.")

        elif choice == "2":
            customer = qu.dequeue()
            if customer is not None: # Help the next customer in the queue and return message that they were helped
                print(f"{customer} has been helped. Next!")
            else:
                print("\nNo customers.")


        elif choice == "3":
            # Peek at the next customer in the queue and return their name
            customer = qu.peek()
            if customer:
                print(f"\n{customer} is the next customer.")
            else:
                print("\nNo customers.")


        elif choice == "4":
            # Print all customers in the queue
            print("\nWaiting customers:")
            qu.print_queue()
            

        elif choice == "5":
            print("Exiting Help Desk System.")
            break
        else:
            print("Invalid option.")

# TESTS

print("\n=== QUEUE TESTS ===")
qu = Queue()

# Edge Case 1: Dequeue when empty
print("Dequeue empty:", qu.dequeue())  # Expect None

# Interaction 1: Enqueue values
qu.enqueue("Alice")
qu.enqueue("Bob")
qu.enqueue("Charlie")
print("After enqueuing Alice, Bob, Charlie:")
qu.print_queue()  # Expect - Alice - Bob - Charlie

# Interaction 2: Peek front
print("Peek:", qu.peek())  # Expect "Alice"

# Interaction 3: Dequeue one
print("Dequeued:", qu.dequeue())  # Expect "Alice"
print("After dequeue:")
qu.print_queue()  # Expect - Bob - Charlie

# Interaction 4: Enqueue more
qu.enqueue("Diana")
print("After enqueue Diana:")
qu.print_queue()  # Expect - Bob - Charlie - Diana

# Interaction 5: Dequeue all until empty (edge case included)
print("Dequeued:", qu.dequeue())  # Bob
print("Dequeued:", qu.dequeue())  # Charlie
print("Dequeued:", qu.dequeue())  # Diana
print("Dequeued empty:", qu.dequeue())  # None
qu.print_queue()  # Expect "Queue is empty"

# END TESTS

if __name__ == "__main__":
    run_help_desk()
