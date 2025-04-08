# Q1
"""
Depth-first search is used to implement topological sorting. 
Topological sort is a linear ordering of the vertices in a directed acyclic graph (DAG) such that for every directed edge u → v, 
vertex u comes before v in the ordering. It helps achieve this because it explores a node's entire path (depth) before backtracking. 
Then, once all descendants of a node are processed, we can safely record that node. Also by pushing nodes to a stack after visiting 
all their neighbors, we ensure that each node is placed after all nodes it depends on.
"""

# from ex1.py
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
    
    # Q2
    def isDAG(self):
        visited = set()
        rec_stack = set()

        def dfs(v):
            visited.add(v)
            rec_stack.add(v)
            neighbors = self.get_neighbors(v)
            for neighbor in neighbors:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
                elif neighbor in rec_stack:
                    return True
            rec_stack.remove(v)
            return False

        for node in self.nodes:
            if node not in visited:
                if dfs(node):
                    return False  # Cycle detected
        return True  # No cycles
    

    def get_neighbors(self, node):
        """Helper to get neighbors from linked list."""
        for adj in self.adjacency:
            if adj.name == node:
                current = adj.head
                neighbors = []
                while current:
                    neighbors.append(current.data)
                    current = current.next
                return neighbors
        return []

    # Q3
    def topoSort(self):
        if not self.isDAG():
            raise Exception("Topological sort not possible: the graph has cycles.")

        visited = set()
        result = []

        def dfs(v):
            visited.add(v)
            neighbors = self.get_neighbors(v)
            for neighbor in neighbors:
                if neighbor not in visited:
                    dfs(neighbor)
            result.append(v)

        for node in self.nodes:
            if node not in visited:
                dfs(node)
        
        result.reverse()
        return result


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


