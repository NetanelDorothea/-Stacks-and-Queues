from node import Node
    
class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        """Adds a new item to the top of the stack"""
        new_node = Node(value)
        new_node.next = self.top # Point to the old top
        self.top = new_node # Move top to the new node

    def pop(self):
        """Removes and returns the item from the top of the stack"""
        if not self.top:
            return None
        removed_node = self.top
        self.top = self.top.next # Move top to the next node
        return removed_node.value	
    
    def peek(self):
        """Returns the value of the Node on the top without removing it."""
        if self.top:
            return self.top.value
        else:
            return None
        
    def print_stack(self):
        """prints out the entire stack"""
        current = self.top
        if not current:
            print("\nStack is empty")
            return
        while current:
            print(f"- {current.value}")
            current = current.next # Update current to next value

    def clear(self):
        """clears the stack"""
        self.top = None    


def run_undo_redo():
    # Create instances of the Stack class for undo and redo
    undo_stack = Stack()
    redo_stack = Stack()

    while True:
        print("\n--- Undo/Redo Manager ---")
        print("1. Perform action")
        print("2. Undo")
        print("3. Redo")
        print("4. View Undo Stack")
        print("5. View Redo Stack")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            action = input("\nDescribe the action (e.g., Insert 'a'): ")
            undo_stack.push(action) # Push the action onto the undo stack and clear the redo stack
            redo_stack.clear() #clears the 'redo' stack
            print(f"Action performed: {action}")

        elif choice == "2":
            undo_value = undo_stack.pop() # Pop an action from the undo stack and push it onto the redo stack
            if undo_value is not None:
                redo_stack.push(undo_value)
                print(f"\nUndid action: {undo_value}")
            else:
                print("\nNothing to undo.")

        elif choice == "3":
            redo_value = redo_stack.pop() # Pop an action from the redo stack and push it onto the undo stack
            if redo_value is not None:
                undo_stack.push(redo_value)
                print(f"\nRedid action: {redo_value}")
            else:
                print("\nNothing to redo.")

        elif choice == "4":
            # Print the undo stack
            print("\nUndo Stack:")
            undo_stack.print_stack()
            
        elif choice == "5":
            # Print the redo stack
            print("\nRedo Stack:")
            redo_stack.print_stack()         
                        
        elif choice == "6":
            print("Exiting Undo/Redo Manager.")
            break
        else:
            print("Invalid option.")


# TESTS

print("=== Testing Stack ===")
stack = Stack()

# Edge Case 1: Pop on empty stack
print("Pop empty:", stack.pop())  # Expect None

# Interaction 1: Push 3 items
stack.push("A")
stack.push("B")
stack.push("C")
print("After pushing A, B, C:")
stack.print_stack()  # Expect - C - B - A

# Interaction 2: Pop 1 item
print("Popped:", stack.pop())  # Expect "C"
print("After pop:")
stack.print_stack()  # Expect - B - A

# Interaction 3: Clear stack
stack.clear()
print("After clear:")
stack.print_stack()  # Expect "Stack is empty"

# Interaction 4: Push after clear
stack.push("X")
print("After pushing X:")
stack.print_stack()  # Expect X

# Interaction 5: Pop until empty
print("Popped:", stack.pop())  # Expect X
print("Popped empty:", stack.pop())  # Expect None
stack.print_stack()  # Expect "Stack is empty"

# END TESTS

if __name__ == "__main__":
    run_undo_redo()