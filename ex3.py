# Exercise 3

# Question 1 has been provided as a pdf

# Question 2
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False  # Cycle detected
        
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        
        return True

def has_cycle(edges, n):
    uf = UnionFind(n)
    
    for edge in edges:
        if not uf.union(edge[0], edge[1]):
            return True  # Cycle detected
    
    return False

# Example usage:
edges = [(0, 1), (1, 2), (2, 0)]  # Example graph with a cycle
n = 3  # Number of nodes in the graph
if has_cycle(edges, n):
    print("Cycle detected!")
else:
    print("No cycle found.")




# Question 3
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
        
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        
        return True

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
    
    def add_edge(self, u, v, w):
        self.graph.append((u, v, w))
    
    def mst(self):
        result = Graph(self.V)
        self.graph.sort(key=lambda x: x[2])
        uf = UnionFind(self.V)
        i = 0
        
        while len(result.graph) < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = uf.find(u)
            y = uf.find(v)
            
            if x != y:
                result.add_edge(u, v, w)
                uf.union(x, y)
        
        return result

# Example usage:
g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

mst_graph = g.mst()

print("Edges in the Minimum Spanning Tree:")
for edge in mst_graph.graph:
    print(edge)
