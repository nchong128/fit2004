import math

class Vertex:
    def __init__(self, num):
        self.num = num
        self.connections = []
        self.banned = False
        self.detour = False

    def ban(self):
        self.banned = True

    def markAsDetour(self):
        self.detour = True

class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.w = weight
        self.banned = False

    def ban(self):
        self.banned = True

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

class Graph:
    def __init__(self):
        '''
        Initial constructor
        Time complexity: O(1)
        Space complexity: O(1)
        Error handle: None
        Return: None
        Parameter: None
        Precondition: None
        '''
        self.graph = []

    def __str__(self):
        final = ""

        for vertex in self.graph:
            final += "{}|".format(vertex.num)

            for edge in vertex.connections:
                final += " --{}--> {},".format(edge.w, edge.v.num)

            final += "\n"

        return final

    def buildGraph(self, filename_roads):
        '''
        This function builds the graph based on a given file
        Time complexity: TODO
        Space complexity: O(E + V)
        Error handle: None
        Return: None
        Parameter: filename_roads: Name of the file to build a graph from
        Precondition: None
        '''

        # Read file and place all info into a table
        file = open(filename_roads, 'r')

        fileInfo = []
        for line in file:
            if len(line) > 0:
                line = line.strip().split(" ")

                line[0] = int(line[0])
                line[1] = int(line[1])
                line[2] = float(line[2])

                fileInfo.append(line)

        file.close()

        # Loop over every line of the file
        for i in range(len(fileInfo)):
            # Check from the vertex IDs in this line whether more vertices need to be made
            if max(fileInfo[i][0], fileInfo[i][1]) + 1 > len(self.graph):
                # Add more vertices based on the line
                newHighestVertex = max(fileInfo[i][0],fileInfo[i][1])

                for j in range(len(self.graph), newHighestVertex + 1):
                    self.graph.append(Vertex(j))

            # Retrieve source vertex based on line
            sourceVertex = self.graph[fileInfo[i][0]]

            # Retrieve target vertex based on line
            targetVertex = self.graph[fileInfo[i][1]]

            # Retrieve weight based on line
            weight = fileInfo[i][2]

            # Add edge between source vertex and target vertex
            sourceVertex.connections.append(Edge(sourceVertex, targetVertex, weight))

    def quickestPath(self, source, target):
        '''
        This function finds the quickest path from a source vertex to a destination vertex
        Time complexity: O(E log V)
        Space complexity: O(E + V)
        Error handle: None
        Return:
            - tuple containing:
                - list(contains nodes in the order of the quickest path traversal from source to target)
                - time storing the total time required from reaching the target from the source
        Parameter:
            - source = String of the source vertex
            - target = String of the target vertex
        Precondition:
            - source and target are valid vertices
        Cases
            - Source = target
            - Normal case
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
            [uMinDist, u] = discovered.extractMin()

            # Ensure the entry is not out of date
            if distances[u] <= uMinDist:
                # Get edges adjacent to current vertex
                adjacentEdges = self.graph[u].connections

                for edge in adjacentEdges:
                    v = edge.v.num
                    edgeWeight = edge.w

                    if distances[v] > distances[u] + edgeWeight:
                        # Update distance entry and add entry to min-heap
                        distances[v] = distances[u] + edgeWeight
                        pred[v] = u
                        discovered.add(distances[v], v)

        # Now find the path from the source to the target and return
        return self.tracePath(srcVertex, tgtVertex, distances, pred)

    def tracePath(self, srcVertex, tgtVertex, distances, pred):
        '''
        This function traces the path from a source vertex to a target vertex
        based on the computed distances and pred lists
        Time complexity: TODO
        Space complexity: TODO
        Error handle: None
        Return:
            - tuple containing:
                - list(contains nodes in the order of the quickest path traversal from source to target)
                - time storing the total time required from reaching the target from the source
        Parameter:
            - srcVertex: Vertex representing the source vertex
            - tgtVertex: Vertex representing the target vertex
            - distances: List of the distance to a given vertex (at the index)
            - pred: List containing the vertex directed toward the vertex at the index
        Precondition:
            - distances and pred are calculated from the caller function

        '''
        # Get total distance
        totalDistance = distances[tgtVertex.num]

        if totalDistance != math.inf:
            # Start at the target vertex and trace backwards
            current = tgtVertex.num
            path = []

            # Keep inserting the vertex until we trace back to the source
            while current != srcVertex.num:
                path.insert(0, current)
                current = pred[current]

            path.insert(0, srcVertex.num)
        else:
            # If the distance to the target is infinite, there is no path there
            return [[],-1]

        return (path, totalDistance)

    def augmentGraph(self, filename_camera, filename_toll):
        '''
        This function changes the graph to now account for banned vertices and
        banned edges.
        Time complexity: TODO
        Space complexity: O(V + E)
        Error handle: None
        Return: None
        Parameter:
            - filename_camera: Name of text file containing list of red-light cameras
            - filename_toll: Name of text file containing the list of tolls
        Precondition:
            - None
        '''
        # Retrieve banned vertices from file
        cameraFile = open(filename_camera, 'r')
        bannedVertices = []
        for line in cameraFile:
            if len(line) > 0:
                bannedVertices.append(int(line.strip()))
        cameraFile.close()

        # Mark vertices as banned
        for vertex in bannedVertices:
            self.graph[vertex].ban()

        # Retrieve banned edges from file
        tollFile = open(filename_toll, 'r')
        bannedEdges = []
        for line in tollFile:
            line = line.strip().split(" ")
            if len(line) == 2:
                line[0] = int(line[0])
                line[1] = int(line[1])
                bannedEdges.append(line)
        tollFile.close()

        # Iterate over edges to ban
        for bannedEdge in bannedEdges:
            # Get source vertex for banned edge
            srcVertex = self.graph[bannedEdge[0]]

            # Search for an edge from source vertex to the target vertex
            for i in range(len(srcVertex.connections)):
                # Match found, mark the edge as banned
                if srcVertex.connections[i].v.num == bannedEdge[1]:
                    edgeToBan = srcVertex.connections[i]
                    edgeToBan.ban()
                    break

    def quickestSafePath(self, source, target):
        '''
        This function finds the quickest path from a source vertex to a destination vertex
        WITH the additional constraint of avoiding banned edges/vertices
        Time complexity: O(E log V)
        Space complexity: O(E + V)
        Error handle: None
        Return:
            - tuple containing:
                - list(contains nodes in the order of the quickest path traversal from source to target)
                - time storing the total time required from reaching the target from the source
        Parameter:
            - source = String of the source vertex
            - target = String of the target vertex
        Precondition:
            - source and target are valid vertices
        Cases
            - Source = target
            - Normal case
            - No vertices banned
            - Source vertex banned
            - Target vertex banned
        '''
        # Get source and target vertex
        srcVertex = self.graph[int(source)]
        tgtVertex = self.graph[int(target)]

        # Early exit if source or target vertex is banned
        if srcVertex.banned or tgtVertex.banned:
            return [[], -1]

        # Initialise lists and min-heap
        distances = [math.inf for i in range(len(self.graph))]
        pred = [0 for i in range(len(self.graph))]

        distances[srcVertex.num] = 0

        discovered = MinHeap()
        discovered.add(0, srcVertex.num)

        # Loop over as long as there is a vertex in the discovered min-heap
        while discovered.count > 0:
            [uMinDist, u] = discovered.extractMin()

            # Ensure the entry is not out of date
            if distances[u] <= uMinDist:
                # Get edges adjacent to current vertex
                adjacentEdges = self.graph[u].connections

                # Filter through outgoing edges and exclude banned vertices and edges
                usableAdjacentEdges = []
                for edge in adjacentEdges:
                    if (not edge.u.banned) and (not edge.banned):
                        usableAdjacentEdges.append(edge)

                for edge in usableAdjacentEdges:
                    v = edge.v.num
                    edgeWeight = edge.w

                    if distances[v] > distances[u] + edgeWeight:
                        # Update distance entry and add entry to min-heap
                        distances[v] = distances[u] + edgeWeight
                        pred[v] = u
                        discovered.add(distances[v], v)

        # Now find the path from the source to the target and return
        return self.tracePath(srcVertex, tgtVertex, distances, pred)

    def addService(self, filename_service):
        # Retrieve detour vertices from file
        vertexFile = open(filename_service, 'r')
        detourVertices = []
        for line in vertexFile:
            if len(line) > 0:
                detourVertices.append(int(line.strip()))
        vertexFile.close()

        # Mark vertices
        for vertex in detourVertices:
            # Get vertex
            pass



        pass

    def quickestDetourPath(self, source, target):
        '''
        Complexity
            - Time O(E log V)
            - Space O(E + V)
        '''
        pass

def main():
    task1FileName = "basicGraph.txt"
    graph = Graph()

    graph.buildGraph(task1FileName)

    # print(graph)

    ### TASK 1
    source, target = "4", "2"
    quickestPathRes = graph.quickestPath(source, target)

    # # print(quickestPathRes)
    #
    # ### TASK 2
    # filename_camera, filename_toll = 'camera.txt', 'toll.txt'
    # graph.augmentGraph(filename_camera, filename_toll)
    # quickestSafePathRes = graph.quickestSafePath(source, target)
    #
    # ### TASK 3
    # filename_service = 'servicePoint.txt'
    # graph.addService(filename_service)

if __name__ == "__main__":
    '''
    --
    Time complexity:
    Space complexity:
    Error handle:
    Return:
    Parameter:
    Precondition:
    '''
    main()
