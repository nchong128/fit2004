import math


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
            sourceVertex.connections.append(Edge(sourceVertex, targetVertex, weight))

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

        -- Should return ([],-1) if path does not exist

        Complexity
        - Time complexity of O(E log V)
        - Space complexity O(E + V) (original graph)
        '''
        # Get source and target vertex
        srcVertex = self.graph[int(source)]
        tgtVertex = self.graph[int(target)]

        # Initialise lists and min-heap
        distances = [math.inf for i in range(len(self.graph))]
        pred = [0 for i in range(len(self.graph))]

        distances[srcVertex.num] = 0

        discovered = MinHeap()
        discovered.add(0, srcVertex.num)

        # Loop over as long as there is a vertex in the discovered min-heap
        while discovered.count > 0:
            [uDist, uNum] = discovered.extractMin()

            # Ensure the entry is not out of date
            if distances[uNum] <= uDist:
                # Get edges adjacent to current vertex
                adjacentEdges = self.graph[uNum].connections

                for edge in adjacentEdges:
                    if distances[edge.v.num] > distances[uNum] + edge.w:
                        # Update distance entry and add entry to min-heap
                        distances[edge.v.num] = distances[uNum] + edge.w
                        pred[edge.v.num] = uNum
                        discovered.add(distances[edge.v.num], edge.v.num)

        # Now find the path from the source to the target and return
        return self.tracePath(srcVertex, tgtVertex, distances, pred)

    def tracePath(self, srcVertex, tgtVertex, distances, pred):
        current = tgtVertex.num
        path = []

        while current != srcVertex.num:
            path.insert(0,current)
            current = pred[current]

        path.insert(0,srcVertex.num)

        # Get total distance too
        totalDistance = distances[tgtVertex.num]

        return (path, totalDistance)

class MinHeap:
    # Acquired from my FIT1008 notes and adjusted to work with
    # (key = distance (int), value = vertex number (int))
    def __init__(self):
        self.array = [None]
        self.count = 0

    def __str__(self):
        return self.array

    def __len__(self):
        return self.count

    def getRoot(self):
        return self.array[1]

    def add(self, key, val):
        self.array.append([key, val])
        self.count += 1
        self.rise(self.count)

    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def rise(self, k):
        while k > 1 and self.array[k][0] < self.array[k//2][0]:
            self.swap(k, k//2)
            k //= 2

    def sink(self, k):
        while 2*k <= self.count:
            child = self.smallestChild(k)
            if self.array[k][0] <= self.array[child][0]:
                break
            self.swap(child, k)
            k = child

    def extractMin(self):
        self.swap(1, self.count)
        min = self.array.pop(self.count)
        self.count -= 1
        self.sink(1)
        return min

    def smallestChild(self, k):
        if 2*k == self.count or self.array[2*k][0] < self.array[2*k+1][0]:
            return 2*k
        else:
            return 2*k + 1

    def replaceRoot(self, newRoot):
        if self.count >= 1:
            oldRoot = self.array[1]
            self.array[1] = newRoot
            self.sink(1)
            return oldRoot

def main():
    filename = "basicGraph.txt"
    directedGraph = DirectedGraph()

    directedGraph.buildGraph(filename)

    print(directedGraph)

    res = directedGraph.quickestPath("4","3")
    print(res)


if __name__ == "__main__":
    main()
