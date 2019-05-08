class Vertex:
    def __init__(self, num):
        self.num = num
        self.connections = []

class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.w = weight

class DirectedGraph:
    def __init__(self, n):
        self.graph = [Vertex(i) for i in range(1,n+1)]

    def addEdge(self, index1, index2, weight):
        # Create new edge
        edge = Edge(self.graph[index1-1], self.graph[index2-1], weight)

        # Ensure list is updated
        self.graph[index1-1].connections.append(self.graph[index2-1])

directedGraph = DirectedGraph(5)
directedGraph.addEdge(1, 3, 7)
directedGraph.addEdge(1, 4, 7)

directedGraph.addEdge(2, 1, 2)
directedGraph.addEdge(2, 5, 6)
directedGraph.addEdge(2, 3, 5)

directedGraph.addEdge(4, 5, 8)

print(directedGraph.graph)








