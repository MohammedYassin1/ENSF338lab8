# Exercise 2

"""
Question 1
Slow Implementation (Linear Search):

In this approach, you could simply use a linear array to represent the queue.
When you need to find the node with the smallest distance, you would iterate through the entire array to find the minimum.
While adding or removing elements from the queue might be straightforward, finding the minimum would require scanning the entire queue each time, resulting in a time complexity of O(n), where n is the number of nodes in the queue.
This method is slow, especially for large graphs, as it involves unnecessary iterations to find the minimum.

Faster Implementation (Priority Queue):

A priority queue is a data structure that maintains a set of elements along with their associated priorities.
You can implement the priority queue using various data structures such as binary heap, Fibonacci heap, or even balanced binary search trees like AVL tree or Red-Black tree.
In the context of Dijkstra's algorithm, the priority of each node would be its current distance from the source.
Using a priority queue allows you to efficiently extract the node with the smallest distance in O(log n) time, where n is the number of elements in the queue.
Inserting and updating priorities in a priority queue also typically have efficient time complexities, often O(log n) as well.
Utilizing a priority queue significantly improves the efficiency of Dijkstra's algorithm compared to a linear search implementation.


In summary, while a slow implementation using linear search is straightforward, it can lead to inefficiencies for larger graphs. On the other hand, a faster implementation using a priority queue ensures better performance by efficiently maintaining the node with the smallest distance at the front of the queue.

"""

# Question 2
# Implementation #1
class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node] = {}

    def add_edge(self, from_node, to_node, weight):
        self.nodes[from_node][to_node] = weight

    def slowSP(self, source):
        # Initialize distances from source to all other nodes as infinity
        distances = {node: float('inf') for node in self.nodes}
        distances[source] = 0  # Distance from source to itself is 0
        visited = set()  # Set to keep track of visited nodes

        while len(visited) < len(self.nodes):
            min_distance = float('inf')
            min_node = None

            # Find the node with the smallest distance (inefficiently)
            for node in self.nodes:
                if node not in visited and distances[node] < min_distance:
                    min_distance = distances[node]
                    min_node = node

            visited.add(min_node)

            # Update distances of neighbors of the current node
            for neighbor, weight in self.nodes[min_node].items():
                if distances[min_node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[min_node] + weight

        return distances



# Implementation #2
class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node] = {}

    def add_edge(self, from_node, to_node, weight):
        self.nodes[from_node][to_node] = weight

    def fastSP(self, source):
        import heapq

        # Initialize distances from source to all other nodes as infinity
        distances = {node: float('inf') for node in self.nodes}
        distances[source] = 0  # Distance from source to itself is 0
        priority_queue = [(0, source)]  # Priority queue to store (distance, node) pairs

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            # If current node has been visited already, skip
            if current_distance > distances[current_node]:
                continue

            # Update distances of neighbors of the current node
            for neighbor, weight in self.nodes[current_node].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances
