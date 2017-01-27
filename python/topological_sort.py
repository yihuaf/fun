import stack
import graph

# Implement a new graph with topological sort.
class Graph(graph.Graph):
    def topologicalSortHelp(self, node, result, visited):
        # mark as visited
        visited[node] = True
        # find all the neighbor
        for v in self.graph[node]:
            if not visited[v]:
                self.topologicalSortHelp(v, result, visited)
        # if no unvisited neighbor, add to result.
        result.push(node)
        return

    def topologicalSort(self):
        result = stack.Stack()
        visited = [False]*self.V
        for node in range (self.V):
            if not visited[node]:
                self.topologicalSortHelp(node, result, visited)
        result.items.reverse()
        return result


def unitTest():
    g = Graph()
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)
    result = g.topologicalSort()
    print(result)

def main():
    unitTest()

if __name__ == "__main__":
    main()
