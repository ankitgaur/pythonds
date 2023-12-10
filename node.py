class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.childrenwitherrors =[]

    def add_child(self, childnode):
        # Add child
        self.children.append(childnode)

    def add_child_with_error(self, childnode):
        # Add child
        self.childrenwitherrors.append(childnode)
        
# Example usage:
if __name__ == "__main__":
    node = Node(name="John")

    # Accessing attributes directly
    print("Parent:", node.name)

    node.add_child("James")
    node.add_child("Richard")

    node.add_child_with_error("Michael")
    node.add_child_with_error("William")

    print("children:", node.children)
    print("childrenwitherrors:", node.childrenwitherrors)

    # Modifying attributes directly
    node.name = "Thomas"
    
    # Printing updated attributes
    print("Updated Name:", node.name)
    