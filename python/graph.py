from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list) # dictionary containing adjacency List
        self.V = 0 # No. of vertices

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.V += 1