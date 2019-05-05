class PrefixTrie:
    def __init__(self, info, isInt):
        if isInt:
            self.size = 10
        else:
            # A = 0, Z = 25, a = 32, z = 57
            self.size = ord('z') - ord('A') + 1

        self.isInt = isInt
        self.root = self.initialiseArray()

        for i in range(len(info)):
            self.insert(info[i], i)

    def initialiseArray(self):
        return PrefixArrayNode(self.size)

    def translateChar(self, char):
        if self.isInt:
            return int(char)
        else:
            return ord(char) - ord('A')

    def insert(self, entry, i):
        current = self.root

        # Loop over every character in the entry
        for char in entry:
            # Get the index of the character based on the trie's type
            index = self.translateChar(char)

            # Create a new array if not present
            if current.array[index] is None:
                current.array[index] = self.initialiseArray()

            # Go down one level
            current = current.array[index]

            # Place index into node
            current.indexList.append(i)

        # Mark off end
        current.isEnd = True

    def retrieve(self, prefix):
        current = self.root

        # Iterate until you get to the array node with given prefix
        depth = 0
        for char in prefix:
            index = self.translateChar(char)

            # If there is an end value at current node
            if current.array[index] is not None:
                depth += 1
                current = current.array[index]

        # Successfully moved down to prefix node -> Get the indexList at that node
        if depth == len(prefix):
            return current.indexList
        else:
            return []

class PrefixArrayNode:
    def __init__(self, size):
        self.array = [None] * size
        self.indexList = []
        self.isEnd = False

def findDuplicates(list1, list2):
    '''
    Finds any elements that are present in both lists
    List is sorted and contains no duplicates
    Cases:
        - One list empty, one not (done)
        - Both lists empty (done)
        - Both lists same size (done)
        - Uneven sized list (done)
        - Both lists with 1 element (done)
    '''
    # Check for empty lists
    if len(list1) == 0 or len(list2) == 0:
        return []

    results = []
    i,j = 0,0

    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            # Match found
            results.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            # Value at i is smaller -> Move pointer i to the right
            i += 1
        else:
            # Value at j is smaller -> Move pointer j to the right
            j += 1

    return results

def query(filename, id_prefix, last_name_prefix):
    '''

    '''

    # Place contents into table and retrieve info
    info = parseInfo(filename)

    # Construct tries based on information
    idTrie = PrefixTrie(info[1], True)
    lastNameTrie = PrefixTrie(info[2], False)

    # Perform queries on tries
    idIndices = idTrie.retrieve(id_prefix)
    lastNameIndices = lastNameTrie.retrieve(last_name_prefix)

    # Find indices that are present in both lists and return
    return findDuplicates(idIndices, lastNameIndices)

def parseInfo(filename):
    # List can be empty
    infoTable = []
    id = []
    lastName = []

    file = open(filename ,'r')

    for line in file:
        line = line.strip().split()
        id.append(line[1])
        lastName.append(line[3])
        infoTable.append(line)
    file.close()

    return [infoTable, id, lastName]

def printFancyTable(table):
    for line in table:
        print(line)

def reverseSubstrings(filename):
    '''
    - File will contain a single line of text (lowercase a-z)
    - Need to find all substrings of length > 1 whose reverse also exists in the text
    - Return a list of lists (each inner list contains two values)
        - First val: substring with length 1 whose reverse exists in the string
        - Second value will be index of the substring in the input text
    - No order requirement

    - Needs to run in O(K^2 + P) time
        - K = total number of characters in the input string
        - P is the total length of all substrings whose reverse appears in the string
    - Space complexity should be O(K^2 + P)
    '''
    file = open(filename, 'r')
    line = file.read()
    file.close()

    print(line)


def main():
    # Task 1
    filename_t1 = 'test1.txt'
    # filename = 'Database.txt'
    id_prefix = '2087652'
    last_name_prefix = 'AB'


    # print(query(filename_t1, id_prefix, last_name_prefix))

    # Task 2
    filename_t2 = 'test2.txt'
    reverseSubstrings(filename_t2)


if __name__ == '__main__':
    main()
