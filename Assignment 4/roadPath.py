class Vertex:
    def __init__(self, num):
        self.num = num
        self.connections = []

class Edge:
    def __init__(self, v, weight):
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

        # Now create Edges between the Vertices based on the info table
        print(fileInfo)

        for i in range(len(fileInfo)):
            # Retrieve source vertex based on line
            sourceVertex = self.graph[int(fileInfo[i][0])]

            # Retrieve target vertex based on line
            targetVertex = self.graph[int(fileInfo[i][1])]

            # Retrieve weight based on line
            weight = float(fileInfo[i][2])

            # Add edge between source vertex and target vertex
            sourceVertex.connections.append(Edge(targetVertex, weight))

        print(self)

    def __str__(self):
        final = ""

        for vertex in self.graph:
            final += "{}|".format(vertex.num)

            for edge in vertex.connections:
                final += " --{}--> {},".format(edge.w, edge.v.num)

            final += "\n"

        return final


def main():
    filename = "basicGraph.txt"
    directedGraph = DirectedGraph()

    directedGraph.buildGraph(filename)


if __name__ == "__main__":
    main()
