class PrefixTrie:
    def __init__(self, info, isInt):
        '''
        This function initialises a prefix trie based on given entries
        Time complexity: Best:
                         Worst:
        Space complexity: Best:
                         Worst:
        Error handling: None
        Precondition: None
        Parameter:
        - info: List of strings representing the entries
        - isInt:
        Return:
        '''

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
        '''
        This function initialises a node to be used in a prefix trie
        Time complexity: Best:
                         Worst:
        Space complexity: Best:
                         Worst:
        Error handling:
        Precondition:
        Parameter:
        Return:
        '''

        return PrefixArrayNode(self.size)

    def translateChar(self, char):
        '''

        Time complexity: Best:
                         Worst:
        Space complexity: Best:
                         Worst:
        Error handling:
        Precondition:
        Parameter:
        Return:
        '''

        if self.isInt:
            return int(char)
        else:
            return ord(char) - ord('A')

    def insert(self, entry, i):
        '''

        Time complexity: Best:
                         Worst:
        Space complexity: Best:
                         Worst:
        Error handling:
        Precondition:
        Parameter:
        Return:
        '''

        current = self.root
        current.indexList.append(i)

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
        '''

        Time complexity: Best:
                         Worst:
        Space complexity: Best:
                         Worst:
        Error handling:
        Precondition:
        Parameter:
        Return:
        '''

        '''
        - make sure all returned indices are integer datatype.
        - Edge cases
        - Both prefixes empty (return all indices)
        - One empty (return results for non-empty prefix)
        '''
        current = self.root

        # If prefix is empty -> No filter is applied so all indices are returned
        if prefix == 0:
            return current.indexList

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

    def retrieveReverseSubstring(self, word):
        results = []

        current = self.root
        count = 0

        for i in range(len(word)):
            char = word[i]
            index = self.translateChar(char)
            count += 1

            # If there is an end value at current node, go to child at index
            if current.array[index] is not None:
                current = current.array[index]
            else:
                break

            # Add word to results if the word has a length >= 2
            if count > 1 and not current.isMarked:
                # Get the index list and add lists to the results
                for wordIndex in current.indexList:
                    results.append([word[:count], int(wordIndex)])

                # Set node as marked
                current.isMarked = True


        return results

class PrefixArrayNode:
    def __init__(self, size):
        '''

        Time complexity: Best:
                         Worst:
        Space complexity: Best:
                         Worst:
        Error handling:
        Precondition:
        Parameter:
        Return:
        '''

        self.array = [None] * size
        self.indexList = []
        self.isEnd = False
        self.isMarked = False

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
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            # Match found
            results.append(int(list1[i]))
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
    This function will query the records found in the file and return the indices of any records that has an ID with the
    given prefix and a last name with the given prefix.
    
    Time complexity: Best: O(T + NM + k + l + nk + nl)
                     Worst: O(T + NM + k + l + nk + nl)
    Space complexity: Best: O(T + NM)
                     Worst: O(T + NM)        
    Error handling: None (handled inside the other functions)
    Precondition:
        - Input file will have indices, ID and phone number as integers
        - First and last names contain only English alphabets
        - Email contains only alpha-numeric values with special characters (@ . - _)
    Parameter:
        - filename (String): The name of the file to retrieve the records
        - id_prefix (String): The prefix that the identification numbers are required to have to be returned
        - last_name_prefix (String): The prefix that the last names are required to have to be returned
    Return:
        - Array of integers that contain the indices that match the given prefixes
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
    '''

    Time complexity: Best:
                     Worst:
    Space complexity: Best:
                     Worst:
    Error handling:
    Precondition:
    Parameter:
    Return:
    '''
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

def reverseString(string):
    reversedString = ""
    for i in range(len(string) - 1, -1, -1):
        reversedString += string[i]
    return reversedString

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
    # Get the string from the file
    file = open(filename, 'r')
    line = file.read()
    file.close()

    # Get the reverse of the line
    reversedLine = reverseString(line)

    # Find all substrings of the string
    substrings = []
    for i in range(len(line)):
        substrings.append(line[i:])

    # Find all substrings of the reversed string
    reversedSubstrings = []

    for i in range(len(reversedLine)):
        reversedSubstrings.append(reversedLine[i:])

    # Create PrefixTrie and insert substrings
    trie = PrefixTrie(substrings, False)

    # Find reversed substrings
    results = []
    for word in reversedSubstrings:
        results = results + trie.retrieveReverseSubstring(word)

    return results

def main():
    # Task 1
    filename_t1 = 'test1.txt'
    # filename = 'Database.txt'
    id_prefix = ''
    last_name_prefix = 'A'

    # query(filename_t1, id_prefix, last_name_prefix)

    # Task 2
    filename_t2 = 'test2.txt'
    ans = reverseSubstrings(filename_t2)

    print(ans)


if __name__ == '__main__':
    '''

    Time complexity: Best:
                     Worst:
    Space complexity: Best:
                     Worst:
    Error handling:
    Precondition:
    Parameter:
    Return:
    '''
    main()

