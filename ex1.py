class Graph:
    def __init__(self):
        self.adjacency = []
        self.nodes = []
    
    def addNode(self, data):
        self.nodes.append(data)
        adj = LinkedList(data)
        self.adjacency.append(adj)
    def removeNode(self, node):
        self.nodes.remove(node)
        for i in self.adjacency:
            if i.name == node:
                self.adjacency.remove(i)
                break
    def addEdge(self, n1, n2, weight): # We need to update both n1 and n2's adjacency lists
        for i in self.adjacency:
            if i.name == n1:
                i.insert(n2, weight)
                break
        for i in self.adjacency:
            if i.name == n2:
                i.insert(n1, weight)
                break


class Node:
    def __init__(self, data, weight):
        self.data = data
        self.weight = weight
        self.next = None

class LinkedList:
    def __init__(self, name):
        self.head = None
        self.name = name

    def insert(self, data, weight):
        """Insert data into the linked list in sorted order."""
        new_node = Node(data, weight)
        if not self.head or self.head.data >= data:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        while current.next and current.next.data < data:
            current = current.next
        
        new_node.next = current.next
        current.next = new_node

    def remove(self, data):
        prev = self.head
        curr = prev
        while curr.data != data:
            prev = curr
            curr = curr.next
        prev.next = curr.next
        curr.next = None

    def display(self):
        """Display the linked list elements."""
        elements = []
        weights = []
        current = self.head
        while current:
            elements.append(current.data)
            weights.append(current.weight)
            current = current.next
        print(f'Elements: {elements}, Weights: {weights}')


if __name__ == '__main__':
    graph1 = Graph()
    graph1.addNode('A')
    graph1.addNode('B')
    graph1.addNode('C')
    graph1.addEdge('A', 'B', 2)
    graph1.addEdge('A', 'C', 6)
    graph1.addEdge('B', 'C', 3)
    
    for i in graph1.adjacency:
        print(f'Node: {i.name}')
        i.display()