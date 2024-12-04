class Stack:
    def __init__(self):
        """Initialize an empty stack."""
        self.items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)
        print(f"Pushed {item} onto the stack.")

    def pop(self):
        """Remove and return the top item of the stack."""
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        return self.items.pop()

    def display(self):
        """Display all items in the stack."""
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack contents (top to bottom):")
            for item in reversed(self.items):
                print(item)

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

stack = Stack()
stack.display()
print(f"Popped item: {stack.pop()}")
stack.display()
