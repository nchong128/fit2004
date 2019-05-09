class PrefixTrie:
    def __init__(self, info, isInt):
        '''
        This function initialises a prefix trie and fills it based on given entries
        Time complexity: Best: O(T) where T is the number of characters in all ID numbers and all last names
                         Worst: O(T)
        Space complexity: Best: O(T)
                         Worst: O(T)
        Error handling: None
        Precondition:
            - info should have entries as all numbers or all strings
        Parameter:
        - info: List of strings representing the entries
        - isInt: Whether the entries are all numbers or not
        Return: None
        '''
        # Sets the node array's size based on if the trie is going to be filled with numbers or letters
        if isInt:
            self.size = 10
        else:
            # A = 0, Z = 25, a = 32, z = 57
            self.size = ord('z') - ord('A') + 1

        self.isInt = isInt
        self.root = self.initialiseArray()

        # Iterate over all entries and insert it into the trie
        for i in range(len(info)):
            self.insert(info[i], i)

    def initialiseArray(self):
        '''
        This function initialises a node to be used in a prefix trie
        Time complexity: Best: O(1)
                         Worst: O(1)
        Space complexity: Best: O(1)
                         Worst: O(1)
        Error handling: None
        Precondition: None
        Parameter: None
        Return: A PrefixArrayNode.
        '''
        return PrefixArrayNode(self.size)

    def translateChar(self, char):
        '''
        This function translates a character into an index value.
        Time complexity: Best: O(1)
                         Worst: O(1)
        Space complexity: Best: O(1)
                         Worst: O(1)
        Error handling: None
        Precondition:
            - char is alphanumeric
        Parameter:
            - char (string) to be converted
        Return:
            - (int) to reference the index in the array
        '''

        if self.isInt:
            return int(char)
        else:
            return ord(char) - ord('A')

    def insert(self, entry, i):
        '''
        This function inserts an entry into the trie. At each node, it will store the value of i. This allows each node
        to store the indices of the entries that uses the node.

        Time complexity: Best: O(N) where N is the length of the entry
                         Worst: O(N)
        Space complexity: Best: O(N)
                         Worst: O(N)
        Error handling: None
        Precondition: Entry is either all numbers or all letters (based on isInt)
        Parameter:
            - entry (String) to be added into the trie
        Return: None
        '''
        # Start at the root
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
        Retrieves the indices of the entries that use a given prefix.

        Time complexity: Best: O(N) where N is the length of the prefix
                         Worst: O(N)
        Space complexity: Best: O(1)
                         Worst: O(1)
        Error handling: If prefix is empty, returns the indexList at the root
        Cases:
            - Prefix is empty -> Retrieve all at root as no 'filter' is applied
            - Prefix does not match against any query -> Returns an empty list
        Precondition: None
        Parameter:
            - prefix (String) to be traversed down the trie in order to find the index list
        Return:
            - indexList (List) that contains the indices that match the prefix
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
        Constructor
        Time complexity: Best: O(1)
                         Worst: O(1)
        Space complexity: Best: O(1)
                         Worst: O(1)
        Error handling: None
        Precondition: None
        Parameter: size of the array
        Return: None
        '''

        self.array = [None] * size
        self.indexList = []
        self.isEnd = False
        self.isMarked = False

def findDuplicates(list1, list2):
    '''
    This function finds any elements that are present in both lists
    Time complexity: Best: O(N + M) where N is the length of the first list and M is the length of the second list
                     Worst: O(N + M)
    Space complexity: Best: O(N + M)
                     Worst: O(N + M)
    Error handling: None
    Cases:
        - One list empty, one not (done)
        - Both lists empty (done)
        - Both lists same size (done)
        - Uneven sized list (done)
        - Both lists with 1 element (done)
    Precondition: Both lists are sorted and contains no duplicates
    Parameter:
        - list1 (list) to be searched for duplicates with the other list
        - list2 (list) to be searched for duplicates with the other list
    Return:
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
    # Place ID and last name into table and retrieve info
    info = parseInfo(filename)

    # Construct tries based on information
    idTrie = PrefixTrie(info[0], True)
    lastNameTrie = PrefixTrie(info[1], False)

    # Perform queries on tries
    idIndices = idTrie.retrieve(id_prefix)
    lastNameIndices = lastNameTrie.retrieve(last_name_prefix)

    # Find indices that are present in both lists and return
    return findDuplicates(idIndices, lastNameIndices)

def parseInfo(filename):
    '''
    This function retrieves the contents of a file for task 1.
    Time complexity: Best: O(NM)
                     Worst: O(NM)
    Space complexity: Best: O(NM)
                     Worst: O(NM)
    Error handling:
        - Returns a list of 2 empty lists if filename is empty
    Precondition:
        - file has the format required for Task 1
    Parameter:
        - filename: Name of the file to extra from
    Return:
        - Table with
            first list containing the IDs of the file
            second list containing the last names of the file
    '''

    # List can be empty
    id = []
    lastName = []

    if len(filename) == 0:
        return [id, lastName]

    # Open and extract file contents
    file = open(filename, 'r')

    for line in file:
        line = line.strip().split()
        id.append(line[1])
        lastName.append(line[3])
    file.close()

    return [id, lastName]

def reverseString(string):
    '''
    This function reverses a string
    Time complexity: Best: O(N) where N is the string's length
                     Worst: O(N)
    Space complexity: Best: O(N)
                     Worst: O(N)
    Error handling: None
    Precondition: None
    Parameter:
        - string (String) to be reversed
    Return: reversed string
    '''
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
    id_prefix = ''
    last_name_prefix = 'A'

    query(filename_t1, id_prefix, last_name_prefix)

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

