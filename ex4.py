# Exercise 4

# This Exercise was completed using the Class graph in Question 1 of exercise 1 instead of using both classes (since not specified which class graph to use)

# Question 1
class Graph2:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.adj_matrix = [[0] * num_nodes for _ in range(num_nodes)]

    def addEdge(self, n1, n2, weight):
        self.adj_matrix[n1][n2] = weight
        self.adj_matrix[n2][n1] = weight  # Assuming undirected graph

    def removeEdge(self, n1, n2):
        self.adj_matrix[n1][n2] = 0
        self.adj_matrix[n2][n1] = 0

    def display(self):
        for row in self.adj_matrix:
            print(row)


# Example usage:
graph2 = Graph2(3)  # Assuming 3 nodes

graph2.addEdge(0, 1, 5)
graph2.addEdge(1, 2, 3)

print("Adjacency Matrix:")
graph2.display()

graph2.removeEdge(0, 1)

print("\nAfter removing edge between nodes 0 and 1:")
graph2.display()


# Question 2
# Extension of Class Graph
class Graph:
    def __init__(self):
        self.nodes = {}

    def addNode(self, data):
        node = GraphNode(data)
        self.nodes[data] = node
        return node

    def removeNode(self, node):
        del self.nodes[node.data]
        for n in self.nodes.values():
            if node.data in n.neighbors:
                del n.neighbors[node.data]

    def addEdge(self, n1, n2, weight=None):
        if n1 not in self.nodes:
            self.addNode(n1)
        if n2 not in self.nodes:
            self.addNode(n2)

        self.nodes[n1].neighbors[n2] = weight
        self.nodes[n2].neighbors[n1] = weight

    def removeEdge(self, n1, n2):
        if n1 in self.nodes and n2 in self.nodes:
            if n2 in self.nodes[n1].neighbors:
                del self.nodes[n1].neighbors[n2]
            if n1 in self.nodes[n2].neighbors:
                del self.nodes[n2].neighbors[n1]

    def dfs(self, start_node):
        visited = set()
        dfs_order = []

        def dfs_util(node):
            nonlocal visited
            nonlocal dfs_order

            visited.add(node)
            dfs_order.append(node)

            for neighbor in self.nodes[node].neighbors:
                if neighbor not in visited:
                    dfs_util(neighbor)

        dfs_util(start_node)
        return dfs_order


# Example usage:
graph = Graph()
node1 = graph.addNode("A")
node2 = graph.addNode("B")
node3 = graph.addNode("C")

graph.addEdge("A", "B", 5)
graph.addEdge("B", "C", 3)

print("DFS traversal:", graph.dfs("A"))


# Extension of Class Graph 2
class Graph2:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.adj_matrix = [[0] * num_nodes for _ in range(num_nodes)]

    def addEdge(self, n1, n2, weight):
        self.adj_matrix[n1][n2] = weight
        self.adj_matrix[n2][n1] = weight  # Assuming undirected graph

    def removeEdge(self, n1, n2):
        self.adj_matrix[n1][n2] = 0
        self.adj_matrix[n2][n1] = 0

    def dfs(self, start_node):
        visited = set()
        dfs_order = []

        def dfs_util(node):
            nonlocal visited
            nonlocal dfs_order

            visited.add(node)
            dfs_order.append(node)

            for neighbor in range(self.num_nodes):
                if self.adj_matrix[node][neighbor] != 0 and neighbor not in visited:
                    dfs_util(neighbor)

        dfs_util(start_node)
        return dfs_order


# Example usage:
graph2 = Graph2(3)  # Assuming 3 nodes

graph2.addEdge(0, 1, 5)
graph2.addEdge(1, 2, 3)

print("DFS traversal:", graph2.dfs(0))
