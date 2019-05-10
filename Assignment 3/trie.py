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
        '''
        This function returns the prefixes that match this given word along with the indices of the last node of that
        word. More detail in the explanations.

        Time complexity: Best: O(NM) == O(P) where N is the length of the longest prefix for the word, the indices
                               at the last letter. NOTE: THIS IS EQUIVALENT TO O(P).
                         Worst: O(NM) == O(P)
        Space complexity: Best: O(NM) == O(P)
                         Worst: O(NM) == O(P)
        Error handling: None
        Precondition: The trie is filled with all of the suffixes of a word
        Parameter:
            - word (String): The word to check any prefixes of that word
        Return:
            - A list containing lists of prefixes that match the word AND the index in which the word occurs
        '''
        results = []

        current = self.root
        count = 0

        # Loop over every letter in the word
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
    Cases:
        - filename is empty [DONE]
        - file is empty [DONE]
        - id_prefix is empty [DONE]
        - last_name_prefix is empty [DONE]
        - Both prefixes empty [DONE]
        - ID is one digit (0-9) [DONE]
        - Last name is one letter (A or z) [DONE]
        - last_name_prefix has different capital letters [DONE]
        - Normal case [DONE]
        - All last names are the same [DONE]
        - id_prefix longer than trie length [DONE]
        - last_name_prefix longer than trie length [DONE]
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
    # Place ID and last name into table and retrieve info               # O(NM)
    info = parseInfo(filename)

    # Construct tries based on information                              # O(T)
    idTrie = PrefixTrie(info[0], True)
    lastNameTrie = PrefixTrie(info[1], False)

    # Perform queries on tries
    idIndices = idTrie.retrieve(id_prefix)                              # O(k + nk)
    lastNameIndices = lastNameTrie.retrieve(last_name_prefix)           # O(l + nl)

    # Find indices that are present in both lists and return            # O(nk + nl)
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
        if len(line) > 0:
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
    This function finds all substrings in the text of length > 1 whose reverse also exists in the text.

    Time complexity: Best: O(K^2 + P) where K is the total number of characters in the file and P is the total length
                           of all substrings whose reverse appears in the string
                     Worst:O(K^2 + P)
    Space complexity: Best:O(K^2 + P)
                     Worst:O(K^2 + P)
    Error handling:
        - Filename is empty -> Return empty list
        - File is empty -> Return empty list
    Cases:
        - File is empty [DONE]
        - filename is empty [DONE]
        - word is one letter long [DONE]
        - extra blank line in file [DONE]
        - two letters [DONE]
        - three letter (e.g. aaa) [DONE]
        - Normal case [DONE]
        - Different capital letters [DONE]
    Precondition: filename contains a single string of alphabets (lowercase only)
    Parameter: filename (String) to find special substrings from
    Return: List containing lists of [substring, index]
    '''
    # If filename is empty
    if len(filename) == 0:
        return []

    # Get the string from the file
    file = open(filename, 'r')
    line = file.readline()
    file.close()

    # If file contents are empty
    if len(line) < 2:
        return []

    # Get the reverse of the line
    reversedLine = reverseString(line)

    # Find all suffixes of the string
    suffixList = []
    for i in range(len(line)):
        suffixList.append(line[i:])

    # Find all suffixes of the reversed string
    reversedSuffixList = []

    for i in range(len(reversedLine)):
        reversedSuffixList.append(reversedLine[i:])

    # Create PrefixTrie and insert normal suffixes
    trie = PrefixTrie(suffixList, False)

    # Find reversed substrings by insertion of reversed suffixes
    results = []
    for word in reversedSuffixList:
        results = results + trie.retrieveReverseSubstring(word)

    return results

def main():
    lineSeparator = '---------------------------------------------------------------------'

    # Task 1
    print('TASK-1:')
    print(lineSeparator)

    task1File = input('Enter the file name of the query database: ')
    id_prefix = input('Enter the prefix of the identification number: ')
    last_name_prefix = input('Enter the prefix of the last name: ')

    indices = query(task1File, id_prefix, last_name_prefix)

    print(lineSeparator)
    print(str(len(indices)) + " record(s) found")
    for index in indices:
        print('Index number: ' + str(index))

    print(lineSeparator)

    # Task 2
    print('TASK-2:')
    task2File = input('Enter the file name for searching reverse substring: ')

    results = reverseSubstrings(task2File)
    resultsStr = ""
    print(lineSeparator)

    if len(results) == 0:
        print("No results found")
    elif len(results) == 1:
        print(str(results[0][0]) + "(" + str(results[0][1]) + ")")
    else:
        for i in range(len(results) - 1):
            resultsStr += str(results[i][0]) + "(" + str(results[i][1]) + ") , "
        resultsStr += str(results[i+1][0]) + "(" + str(results[i+1][1]) + ")"
        print(resultsStr)

    print(lineSeparator)
    print('PROGRAM END')

if __name__ == '__main__':
    main()

