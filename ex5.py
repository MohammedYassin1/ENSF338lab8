# Exercise 5

"""
Question 1

Topological sorting is typically implemented using the Depth-First Search (DFS) algorithm. This algorithm is commonly used because it efficiently visits all vertices and edges of a graph, allowing it to explore the graph's structure and identify the ordering of vertices according to their dependencies.

Here's why DFS is commonly used for topological sorting:

Depth-First Search (DFS) Visits Vertices in Depth-First Order: DFS systematically explores the vertices of the graph by first visiting a vertex, then recursively exploring as far as possible along each branch before backtracking. This property makes it suitable for identifying the order in which vertices can be visited based on their dependencies.

Backtracking Helps Identify Dependencies: As DFS traverses the graph, it uses backtracking to explore all possible paths. During this process, DFS can identify cycles in the graph, which are not allowed in a directed acyclic graph (DAG). This ability to detect cycles is crucial for ensuring the correctness of the topological sorting algorithm.

Ordering Vertices Based on Finishing Times: In a DFS traversal of a graph, vertices are assigned finishing times based on when they are completely explored. Vertices with higher finishing times are explored first, indicating they have fewer dependencies. This property is exploited in topological sorting, where vertices are sorted based on their finishing times in reverse order.

Linear Time Complexity: DFS has a time complexity of O(V + E), where V is the number of vertices and E is the number of edges. Since topological sorting can be performed as a part of DFS with the same time complexity, it is efficient for large graphs.

Overall, the DFS algorithm's ability to systematically traverse the graph, identify dependencies, and detect cycles makes it well-suited for implementing topological sorting.
"""



# Question 2
# Extension of 1st Class
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

    def removeEdge(self, n1, n2):
        if n1 in self.nodes and n2 in self.nodes:
            if n2 in self.nodes[n1].neighbors:
                del self.nodes[n1].neighbors[n2]

    def isdag(self):
        visited = set()
        stack = set()

        def dfs(node):
            if node in stack:
                return False  # Cycle detected
            if node in visited:
                return True  # Already visited and no cycle found from this node

            visited.add(node)
            stack.add(node)

            for neighbor in self.nodes[node].neighbors:
                if not dfs(neighbor):
                    return False  # Cycle detected in this branch

            stack.remove(node)
            return True

        for node in self.nodes:
            if not dfs(node):
                return False  # Cycle detected

        return True  # No cycles found in the graph

# Example usage:
graph = Graph()
node1 = graph.addNode("A")
node2 = graph.addNode("B")
node3 = graph.addNode("C")

graph.addEdge("A", "B", 5)
graph.addEdge("B", "C", 3)

print("Is DAG:", graph.isdag())  # Output: True

graph.addEdge("C", "A", 2)  # Adding an edge to create a cycle

print("Is DAG:", graph.isdag())  # Output: False



# Extension of 2nd class
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

    def importFromFile(self, file):
        self.nodes = {}  # Clear existing nodes
        with open(file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line.startswith("node"):
                    _, node = line.split('[')
                    node = node.split(']')[0].split('=')[1].strip()
                    self.addNode(node)
                elif line.startswith("edge"):
                    _, edge = line.split('[')
                    edge = edge.split(']')[0].split('=')[1].strip()
                    n1, n2, weight = edge.split(',')
                    n1 = n1.strip()
                    n2 = n2.strip()
                    weight = weight.strip()
                    self.addEdge(n1, n2, weight)

    def isdag(self):
        visited = set()
        stack = set()

        def dfs(node):
            if node in stack:
                return False  # Cycle detected
            if node in visited:
                return True  # Already visited and no cycle found from this node

            visited.add(node)
            stack.add(node)

            for neighbor in self.nodes[node].neighbors:
                if not dfs(neighbor):
                    return False  # Cycle detected in this branch

            stack.remove(node)
            return True

        for node in self.nodes:
            if not dfs(node):
                return False  # Cycle detected

        return True  # No cycles found in the graph

# Example usage:
graph = Graph()
graph.importFromFile("example_graph.gv")

print("Is DAG:", graph.isdag())




# Question 3
# Extension of 1st class
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

    def toposort(self):
        visited = set()
        stack = []
        for node in self.nodes.values():
            if node not in visited:
                if not self._dfs(node, visited, stack):
                    return None  # Graph is not a DAG
        return stack[::-1]

    def _dfs(self, node, visited, stack):
        visited.add(node)
        for neighbor in node.neighbors:
            if neighbor not in visited:
                if not self._dfs(self.nodes[neighbor], visited, stack):
                    return False
            elif self.nodes[neighbor] in stack:
                return False  # Cycle detected
        stack.append(node)
        return True

# Example usage:
graph = Graph()
node1 = graph.addNode("A")
node2 = graph.addNode("B")
node3 = graph.addNode("C")

graph.addEdge("A", "B", 5)
graph.addEdge("B", "C", 3)

print("Nodes:", [node.data for node in graph.nodes.values()])
print("Edges from A:", [(neighbor, weight) for neighbor, weight in graph.nodes["A"].neighbors.items()])
print("Edges from B:", [(neighbor, weight) for neighbor, weight in graph.nodes["B"].neighbors.items()])

graph.removeNode(node2)

print("\nAfter removing node B:")
print("Nodes:", [node.data for node in graph.nodes.values()])

print("\nTopological Order:", [node.data for node in graph.toposort()])



# Extension of 2nd class
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

    def importFromFile(self, file):
        self.nodes = {}  # Clear existing nodes
        with open(file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line.startswith("node"):
                    _, node = line.split('[')
                    node = node.split(']')[0].split('=')[1].strip()
                    self.addNode(node)
                elif line.startswith("edge"):
                    _, edge = line.split('[')
                    edge = edge.split(']')[0].split('=')[1].strip()
                    n1, n2, weight = edge.split(',')
                    n1 = n1.strip()
                    n2 = n2.strip()
                    weight = weight.strip()
                    self.addEdge(n1, n2, weight)

    def toposort(self):
        visited = set()
        stack = []
        for node in self.nodes.values():
            if node not in visited:
                if not self._dfs(node, visited, stack):
                    return None  # Graph is not a DAG
        return stack[::-1]

    def _dfs(self, node, visited, stack):
        visited.add(node)
        for neighbor in node.neighbors:
            if neighbor not in visited:
                if not self._dfs(self.nodes[neighbor], visited, stack):
                    return False
            elif self.nodes[neighbor] in stack:
                return False  # Cycle detected
        stack.append(node)
        return True

# Example usage:
graph = Graph()
graph.importFromFile("example_graph.gv")

print("Nodes:", [node.data for node in graph.nodes.values()])
for node in graph.nodes.values():
    print("Edges from", node.data + ":", [(neighbor, weight) for neighbor, weight in node.neighbors.items()])

print("\nTopological Order:", [node.data for node in graph.toposort()])

