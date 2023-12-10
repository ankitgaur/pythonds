class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Error: Stack is empty.")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Error: Stack is empty.")

    def size(self):
        return len(self.items)

# Example usage:
if __name__ == "__main__":
    stack = Stack()

    print("Is the stack empty?", stack.is_empty())

    stack.push("one")
    stack.push("two")
    stack.push("three")

    print("Stack size:", stack.size())
    print("Top of the stack:", stack.peek())

    popped_item = stack.pop()
    print("Popped item:", popped_item)

    print("Stack size after pop:", stack.size())

    popped_item = stack.pop()
    print("Popped item:", popped_item)

    print("Stack size after pop:", stack.size())

    popped_item = stack.pop()
    print("Popped item:", popped_item)

    print("Stack size after pop:", stack.size())
