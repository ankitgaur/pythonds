from node import Node as Node
from map import Map as Map
from queue import Queue as Queue

class Tree:
    def __init__(self):
        self.root = None
        self.node_count = 0
        #TODO: why have this? Always -1 node_count?
        self.children_count = 0
        self.treemap = Map()

    def traverse_bfs(self):
        result = []
        if self.root:

            queue = Queue()
            queue.enqueue(self.root.name)
            
            while queue.size() > 0:
                el = queue.dequeue()
                if el:
                    result.append(el)

                    for child in self.treemap.get(el).children:
                        queue.enqueue(child)

        return result
    
    def traverse_dfs(self, nodename=None):
        result = []

        if not nodename:
            nodename = self.root.name
        
        node = self.treemap.get(nodename)
        result.append(node.name)

        for child in node.children:
            if child:
                tmp = self.traverse_dfs(child)
                result.extend(tmp)

        return result
    
    def add_root(self,parent,child):
        r = Node(parent)
        self.root = r
        self.treemap.push(parent,r)
        self.node_count += 1

        self.add_child(parent,child)

    def add_child(self,parent,child):
        p = self.treemap.get(parent)
        p.add_child(child)
        
        c = Node(child)
        self.treemap.push(child,c)
        self.node_count += 1
        self.children_count += 1
    
    def add_node(self, parent,child=None):
        
        #Tree with members
        if self.treemap.get(parent):
            print(f"Found a parent {parent} for child {child}")
            if child:
                self.add_child(parent,child)

        #This tree already has a root
        #Orphan child aka child with errors
        elif self.root:
            print(f"Parent not found : {parent}")
            print(f"Orpahan Child : {child}")

        #Empty Tree
        elif self.node_count == 0:
            print(f"Empty Tree!! This is a root node. {parent}:{child}")
            self.add_root(parent,child)


# Example usage:
if __name__ == "__main__":
    # Creating a tree
    tree = Tree()

    tree.add_node("one")

    tree.add_node("one","two")
    tree.add_node("one","three")

    #############################

    tree.add_node("two","four")
    tree.add_node("two","five")

    tree.add_node("three","six")
    tree.add_node("three","seven")

    #############################

    tree.add_node("four","eight")
    tree.add_node("four","nine")

    tree.add_node("five","ten")
    tree.add_node("five","eleven")

    tree.add_node("six","twelve")
    tree.add_node("six","thirteen")

    tree.add_node("seven","fourteen")
    tree.add_node("seven","fifteen")

    print(tree.traverse_bfs())
    print(tree.traverse_dfs())
