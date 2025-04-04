# Q2
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False  # Cycle detected

        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        elif self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1

        return True

# Q3
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((weight, u, v))

    def mst(self):
        self.edges.sort()  # Sort by weight
        uf = UnionFind(self.V)
        mst_graph = Graph(self.V)

        for weight, u, v in self.edges:
            if uf.union(u, v):
                mst_graph.add_edge(u, v, weight)

        return mst_graph

    def print_graph(self):
        for weight, u, v in self.edges:
            print(f"{u} -- {v} == {weight}")


# Example usage
if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 2, 2)
    g.add_edge(1, 3, 5)
    g.add_edge(2, 3, 5)
    g.add_edge(2, 4, 11)
    g.add_edge(3, 4, 2)
    g.add_edge(3, 5, 1)
    g.add_edge(4, 5, 7)

    print("Original Graph:")
    g.print_graph()

    mst = g.mst()
    print("\nMinimum Spanning Tree:")
    mst.print_graph()