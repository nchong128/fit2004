import math

class Vertex:
    def __init__(self, num):
        self.num = num
        self.connections = []
        self.banned = False

    def ban(self):
        self.banned = True


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
        self.edgeList = []
        self.highestVertexNum = 0
        self.servicePoints = []

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
                self.highestVertexNum = max(fileInfo[i][0],fileInfo[i][1])

                for j in range(len(self.graph), self.highestVertexNum + 1):
                    self.graph.append(Vertex(j))

            # Retrieve source vertex based on line
            sourceVertex = self.graph[fileInfo[i][0]]

            # Retrieve target vertex based on line
            targetVertex = self.graph[fileInfo[i][1]]

            # Retrieve weight based on line
            weight = fileInfo[i][2]

            # Create Edge and store in edgeList
            edge = Edge(sourceVertex, targetVertex, weight)

            self.edgeList.append(edge)

            # Add edge to connections for source vertex
            sourceVertex.connections.append(edge)

    def rebuildGraph(self):
        # Create new graph
        newGraph = [Vertex(i) for i in range(self.highestVertexNum + 1)]

        # Iterate over every edge in edgeList
        for edge in self.edgeList:
            # Get source and target's number
            srcNum = edge.u.num
            tgtNum = edge.v.num

            # Reassign edge to new graph's vertices
            edge.u = newGraph[srcNum]
            edge.v = newGraph[tgtNum]

            # Add Edge to source vertex's connection list
            edge.u.connections.append(edge)

        # Make newGraph the current graph
        self.graph = newGraph

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
        for vertexId in bannedVertices:
            self.graph[vertexId].ban()

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
        for edgeId in bannedEdges:
            # Get source vertex for banned edge
            srcVertex = self.graph[edgeId[0]]

            # Search for an edge from source vertex to the target vertex
            for i in range(len(srcVertex.connections)):
                # Match found, mark the edge as banned
                if srcVertex.connections[i].v.num == edgeId[1]:
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
        self.servicePoints = []
        for line in vertexFile:
            if len(line) > 0:
                self.servicePoints.append(int(line.strip()))
        vertexFile.close()

    def reverseAllEdges(self):
        for edge in self.edgeList:
            edge.u, edge.v = edge.v, edge.u

    def quickestDetourPath(self, source, target):
        '''
        Complexity
            - Time O(E log V)
            - Space O(E + V)
        '''

        ### Run forward Dijkstra's and save distances and pred
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

        forwardRes = [distances, pred]

        ### Reverse all edges
        self.reverseAllEdges()
        self.rebuildGraph()

        ### Run backward's Dijkstra's and save distances and pred
        # Get source and target vertex  (THIS IS REVERSED)
        srcVertex = self.graph[int(target)]
        tgtVertex = self.graph[int(source)]

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

        backwardRes = [distances, pred]


        # print(forwardRes)
        # print(backwardRes)

        ### Count all distances to the service points
        minDistance = math.inf
        minServicePoint = None
        for num in self.servicePoints:
            totalDistance = forwardRes[0][num] + backwardRes[0][num]
            # Compare against min and update if smaller
            if totalDistance < minDistance:
                minServicePoint = num
                minDistance = totalDistance

        # Early exit if no path
        if minDistance == math.inf or minServicePoint == None:
            return [[],-1]

        # Get path results from source to service
        forwardPath = self.tracePath(self.graph[int(source)], self.graph[minServicePoint], forwardRes[0], forwardRes[1])[0]

        # Remove service point (to avoid duplicates)
        forwardPath.pop()

        # Get path results from target to service
        backwardPath = self.tracePath(self.graph[int(target)], self.graph[minServicePoint], backwardRes[0], backwardRes[1])[0]


        # Reverse backward path so it's service point to target
        self.reverseList(backwardPath)
        #
        # print(forwardPath)
        # print(backwardPath)

        # Combine paths and distance and return
        return (forwardPath + backwardPath, minDistance)







        # task 3
        # --------
        # - Run from source to target (E log V)
        # - Reverse all edges (E)
        # - Then rebuild graph (E)
        # - Run from target to source (E log V)
        # - Count all distances to the service point(V)
        #
        # -fix up graph

    def reverseList(self, list):
        for i in range(len(list)//2):
            list[i], list[len(list) -1 - i] = list[len(list) -1 - i], list[i]


def main():
    task1FileName = "custom/basicGraph.txt"
    graph = Graph()

    graph.buildGraph(task1FileName)

    # print(graph)

    ### TASK 1
    source, target = "4", "2"
    quickestPathRes = graph.quickestPath(source, target)

    # print(quickestPathRes)

    ### TASK 2
    filename_camera, filename_toll = 'custom/camera.txt', 'custom/toll.txt'
    graph.augmentGraph(filename_camera, filename_toll)
    quickestSafePathRes = graph.quickestSafePath(source, target)

    ### TASK 3
    filename_service = 'custom/servicePoint.txt'
    graph.addService(filename_service)
    quickestDetourPathRes = graph.quickestDetourPath(source, target)

    # print(quickestDetourPathRes)



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
