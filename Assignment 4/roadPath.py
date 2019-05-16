# class Vertex:
#     def __init__(self, num):
#         self.num = num
#         self.connections = []
#
# class Edge:
#     def __init__(self, u, v, weight):
#         self.u = u
#         self.v = v
#         self.w = weight
#
# class DirectedGraph:
#     def __init__(self, n):
#         self.graph = [Vertex(i) for i in range(1,n+1)]
#
#     def addEdge(self, index1, index2, weight):
#         # Create new edge
#         edge = Edge(self.graph[index1-1], self.graph[index2-1], weight)
#
#         # Ensure list is updated
#         self.graph[index1-1].connections.append(self.graph[index2-1])

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
    def __init__(self):
        self.graph = []

    def buildGraph(self, filename_roads):
        # Read file and place info all into a table
        file = open(filename_roads, 'r')

        fileInfo = []
        for line in file:
            line = line.strip().split(" ")
            fileInfo.append(line)

        file.close()

        # Retrieve number of vertices to make based on the last row
        numOfVertices = int(fileInfo[-1][0]) + 1

        # Make Vertex instances and add to graph attribute
        for i in range(numOfVertices):
            self.graph.append(Vertex(i))

        print(self.graph)

        pass

def main():
    filename = "basicGraph.txt"
    directedGraph = DirectedGraph()

    directedGraph.buildGraph(filename)


if __name__ == "__main__":
    main()
