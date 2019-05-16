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

            line[0] = int(line[0])
            line[1] = int(line[1])
            line[2] = float(line[2])

            fileInfo.append(line)

        file.close()

        # Retrieve number of vertices to make based on the last row
        numOfVertices = fileInfo[-1][0] + 1

        # Make Vertex instances and add to graph attribute
        for i in range(numOfVertices):
            self.graph.append(Vertex(i))

        # Now create Edges between the Vertices based on the info table
        for i in range(len(fileInfo)):
            # Retrieve source vertex based on line
            sourceVertex = self.graph[fileInfo[i][0]]

            # Retrieve target vertex based on line
            targetVertex = self.graph[fileInfo[i][1]]

            # Retrieve weight based on line
            weight = fileInfo[i][2]

            # Add edge between source vertex and target vertex
            sourceVertex.connections.append(Edge(targetVertex, weight))

    def __str__(self):
        final = ""

        for vertex in self.graph:
            final += "{}|".format(vertex.num)

            for edge in vertex.connections:
                final += " --{}--> {},".format(edge.w, edge.v.num)

            final += "\n"

        return final

    def quickestPath(self, source, target):
        '''
        :param source: Starting point of the travel
        :param target: Destination point of the travel
        :return:
        tuple:
        - list(contains nodes in the order of the quickest path traversal from source to target)
        - time storing the total time required from reaching the target from the source
        '''
        pass


def main():
    filename = "basicGraph.txt"
    directedGraph = DirectedGraph()

    directedGraph.buildGraph(filename)


if __name__ == "__main__":
    main()
