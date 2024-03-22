# Exercise 1

# Question 1
class GraphNode:
    def __init__(self, data):
        self.data = data
        self.neighbors = {}  # Adjacency list

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




# Question 2
class GraphNode:
    def __init__(self, data):
        self.data = data
        self.neighbors = {}  # Adjacency list

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

# Example usage:
graph = Graph()
graph.importFromFile("example_graph.gv")

print("Nodes:", [node.data for node in graph.nodes.values()])
for node in graph.nodes.values():
    print("Edges from", node.data + ":", [(neighbor, weight) for neighbor, weight in node.neighbors.items()])
