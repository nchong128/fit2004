def wordInList(word, list):
    '''
    Finds whether a word (or character is in a list
    Time complexity: O(n) in the worst case where n = len(list)
    Space complexity: O(1) in the worst case as no list is passed by reference and only one
        String variable will be created
    Error handling: N/A
    Parameters:
        word (String): Item to be searched for
        list (List): Container to search the word in
    Return:
        Boolean: True if the item is in the list. False otherwise
    '''
    for i in range(len(list)):
        if word == list[i]:
            return True
    return False

def preprocess(fileName):
    '''
    This function is process the contents of a given file into a list of words, removing any
    banned punctuation, aux verbs, and articles.
    Time complexity: O(nm) at the worst case. Explanation covered in Analysis.pdf.
    Space complexity: O(nm) at the worst case. Explanation covered in Analysis.pdf.
    Error handling:
        Returns empty list if no contents in file.
    Parameters:
        fileName (String): The name of the file to extract the contents from
    Return:
        List: List of words after pre-processing (i.e. no banned things)
    '''
    # Lists containing banned words and punctuations
    bannedWords = ['am', 'is', 'are', 'was', 'were', 'has', 'have', 'had', 'been', 'will', 'shall', 'may', 'can', 'would', 'should', 'might', 'could','a', 'an', 'the','']
    bannedPunctuation = [',', '.', '?', '!', ':', ';', '"',' ', '\n', '\t']

    # Extract a string containing all of the content from the file
    file = open(fileName, 'r')
    fileContent = file.read()
    file.close()

    # Return empty list if no content in file
    if len(fileContent) == 0:
        return []

    # Iterate over file contents and remove punctuations
    temp = []
    word = ""

    for i in range(len(fileContent)):
        letter = fileContent[i]
        if wordInList(letter, bannedPunctuation):
            temp.append(word)
            word = ""
        else:
            word += letter

    # Cover up for any built-up words that was not added
    if len(word) > 0:
        temp.append(word)

    # Iterate over the output list and remove the banned words
    output = []
    for i in range(len(temp)):
        word = temp[i]

        if not wordInList(word, bannedWords):
            output.append(word)

    return output

def largestElement(list):
    '''
    This function returns the largest element in a list (where it is based on Python's > comparator)
    Time complexity: O(nm) where n = len(list) as it iterates over every element in the list and does an O(m) string
    comparison
    Space complexity: O(1) as the list is passed by reference and a constant number of variables are being created,
        regardless of n
    Error handling: N/A
    Parameters:
        list (List): Contains the elements to find the largest of.
    Return:
        String/Number: The largest element in the list
    '''
    indexOfLargest = 0
    largestWord = list[0]

    # Iterate through the rest of the list
    for i in range(1, len(list)):

        # Choose the new largest if the current element is larger than the current largest
        if len(list[i]) > len(largestWord):
            indexOfLargest = i
            largestWord = list[i]

    return largestWord

def makeOrdKey(list,index):
    '''
    This function gives a list of keys based on the character at the index of the given list
    Time complexity: O(n) where n = len(list) as it iterates over every element in the list
    Space complexity: O(n) where n  = len(list) as keyList will contain the number of items as the list param.
    Error handling: N/A
    Parameters:
        list (List): Where the extract the character and turn into a key
        index (Integer): The position of the string to extract the character from
    Return:
        List: A list where each element is an ord value for the character at the specified index for the word at the same
        position as the list param
    '''
    offset = 96     # offset customised such that ` = 0, a = 1, b = 2, ...
    keyList = []

    for item in list:
        # Convert char to ord value, apply offset and append to list
        keyList.append(ord(item[index]) - offset)

    return keyList

def fillWithChar(word, intendedSize):
    '''
    This function inflates a word with the backtick (`) character until it is of the intended size
    Time complexity: O(n) where n = intendedSize as the word will have to be filled up to n-1 times (from 1 character)
    Space complexity: O(1) as there will always be the same number of variables regardless of the input size, and the
        parameters are not arrays so the input size is constant
    Error handling: N/A
    Parameters:
        word (String): Word to be inflated
        intendedSize (integer): The intended size that the word parameter should be
    Return:
        word (String): The word inflated with backticks until it is of the intended size
    '''

    specialChar = "`"
    difference = intendedSize - len(word)

    for i in range(difference):
        word = word + specialChar

    return word

def removeChar(word):
    '''
    This function removes the backtick (`) from a word
    Time complexity: O(n) where n = len(word) as it iterates through the length of the word
    Space complexity: O(1) as the number of variables remain constant and the input parameter is a string of fixed size
    Error handling: N/A
    Parameters:
        word (String): Word to remove the backticks
    Return:
        String: The word but without the special characters at the end
    '''
    specialChar = "`"

    newWord = ""

    for letter in word:
        if letter == specialChar:
            break
        newWord = newWord + letter
    return newWord

def countingSort(list, index):
    '''
    This function applies counting sort to a list, sorting it based on a given index in which to base the key off
    Time complexity:
        O(n) where n is len(list). Making the key list will take O(n) time, iterating over the keys and appending to the
        count table will also take O(n). It then takes O(d),where d is a constant 27, to iterate over the count table.
        So O(n) + O(n) + O(d) = O(n).
    Space complexity:
        O(n) where n = len(list). The input size is hence O(n) + O(1) = O(n). The keyList and table will be O(n) and O(2n)
        as it is based off the input list. Once count is filled from the table, it will be O(n). The output list
        contains the same number of elements as the count so it is also O(n). O(n) + O(n) + O(2n) + O(n) + O(n) = O(n)
    Error handling: N/A
    Parameters:
        list (List): The list to be sorted through
        index (integer): The index in which to base the key off
    Return:
        List: similar to the list parameter, but sorted based on the index as the key
    '''
    # Create empty table containing 27 lists
    count = [[] for i in range(27)]

    # Create the key list based on the index
    keyList = makeOrdKey(list, index)

    # Create table consisting of key list and input list
    table = [keyList, list]

    # Iterate over every key in the list and place into count based on acquired key
    for i in range(len(table[0])):
        key = table[0][i]
        val = table[1][i]
        count[key].append([key, val])

    # Iterate over every list in count and place the value back
    output = []
    for list in count:
        if len(list) > 0:
            for elem in list:
                output.append(elem[1])

    return output

def wordSort(preprocessedWordList):
    '''
    This function will sort the word list in alphabetical order
    Time complexity: O(nm) at the worst case. Explanation covered in Analysis.pdf.
    Space complexity: O(nm) at the worst case. Explanation covered in Analysis.pdf.
    Error handling: N/A
    Parameters:
        preprocessedWordList (List): List of words to be sorted
    Return:
        List: preProcessedWordList but sorted in alphabetical order
    '''
    # If the list is just 1 element long -> Return the same list
    if len(preprocessedWordList) == 1:
        return preprocessedWordList

    # Get the largest element in the list and the length of it
    largestElem = largestElement(preprocessedWordList)
    lenOfLargest = len(largestElem)

    # Fill words that are not the largest size with a special character ` from the right
    for i in range(len(preprocessedWordList)):
        word = preprocessedWordList[i]
        if (len(word) < lenOfLargest):
            preprocessedWordList[i] = fillWithChar(word, lenOfLargest)

    # Use radix sort on the strings, with counting sort on a specified index of the words
    for i in range(lenOfLargest -1 , -1, -1):
        preprocessedWordList = countingSort(preprocessedWordList, i)

    # Remove special character `
    for i in range(len(preprocessedWordList)):
        preprocessedWordList[i] = removeChar(preprocessedWordList[i])

    return preprocessedWordList

def wordCount(sortedList):
    '''
    This function counts the number of occurrences for each word in a sorted list, printing and returning the results
    in a list.
    Time complexity: O(nm) at the worst case. Explanation covered in Analysis.pdf.
    Space complexity: O(nm) at the worst case. Explanation covered in Analysis.pdf.
    Error handling: N/A
    Parameters:
        sortedList (List): List containing words sorted in the alphabetical order to count the number of occurences
    Return:
        List: First element contains the total number of words, the rest of the list contains a list containing a word
        and the number of occurrences for that word.
    '''
    # Initial values to be returned
    wordsAndCounts = [0]

    # Iterate over all words in the sortedList
    for word in sortedList:
        wordsAndCounts[0] += 1     # increase total number of words

        if len(wordsAndCounts) == 1 or wordsAndCounts[-1][0] != word:
            # initiate word and a initial count of 1 if the word is not in the output list
            wordsAndCounts.append([word,1])
        elif wordsAndCounts[-1][0] == word:
            # continue increasing the number of occurences
            wordsAndCounts[-1][1] += 1

    # Print and return list
    print("\nThe total number of words in the writing: " + str(wordsAndCounts[0]))
    print("The frequencies of each word:")
    printKeyValueTable(wordsAndCounts[1:])

    return wordsAndCounts

class MinHeap:
    # Acquired from my FIT1008 notes and adjusted to work with key-value arrays
    def __init__(self):
        self.array = [None]
        self.count = 0

    def __str__(self):
        return self.array

    def __len__(self):
        return self.count

    def getRoot(self):
        return self.array[1]

    def add(self, item):
        self.array.append(item)
        self.count += 1
        self.rise(self.count)

    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def rise(self, k):
        while k > 1 and self.array[k] < self.array[k//2]:
            self.swap(k, k//2)
            k //= 2

    def sink(self, k):
        while 2*k <= self.count:
            child = self.smallestChild(k)
            if self.array[k] <= self.array[child]:
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
        if 2*k == self.count or self.array[2*k] < self.array[2*k+1]:
            return 2*k
        else:
            return 2*k + 1

    def replaceRoot(self, newRoot):
        if self.count >= 1:
            oldRoot = self.array[1]
            self.array[1] = newRoot
            self.sink(1)
            return oldRoot

def kTopWords(k, sortedWithFreqList):
    '''
    This function will find and display the k-top most frequent words in the writing
    Time complexity: O(n log k) at the worst case. Explanation covered in Analysis.pdf.
    Space complexity: O(km) at the worst case. Explanation covered in Analysis.pdf.
    Error handling: If k is more than the possible number of returnable results, it displays the maximum number of
        results
    Parameters:
        k (integer): The number of top words to display
        sortedWithFreqList (List): The list containing the words and their frequencies
    Return:
        List: Contains the k top words and their frequencies in descending order
    '''
    # CREDIT: Courtesy of Shams' help
    # Create a min heap to handle the lists
    minHeap = MinHeap()

    # Limit k to the max possible number of results
    if k > len(sortedWithFreqList):
        k = len(sortedWithFreqList)

    # Find largest frequency in the list
    maxFreq = sortedWithFreqList[0][1]
    for i in range(len(sortedWithFreqList)):
        if sortedWithFreqList[i][1] > maxFreq:
            maxFreq = sortedWithFreqList[i][1]

    # Make number of lists from 1..maxFreq to hold the words # O(
    wordList = [[] for i in range(maxFreq + 1)]

    # Insert k number of keys into the Heap
    for i in range(k):
        key = sortedWithFreqList[i][1]
        val = sortedWithFreqList[i][0]

        wordList[key].append(val)
        minHeap.add(sortedWithFreqList[i][1])

    # Iterate over from k to the end of the list
    for i in range(k, len(sortedWithFreqList)):
        key = sortedWithFreqList[i][1]
        if key > minHeap.getRoot():
            oldRoot = minHeap.replaceRoot(sortedWithFreqList[i][1])
            # Pop the last value at the position oldRoot
            wordList[oldRoot].pop()
            # Add the new word into the position based on its value
            wordList[key].append(sortedWithFreqList[i][0])

    # Get the keys
    keyList = []
    for i in range(k):
        keyList.append(minHeap.extractMin())

    # Pop the keys and get the value from the wordList into results
    results = []
    for i in range(len(keyList)):
        freq = keyList.pop()
        word = wordList[freq].pop(0)

        results.append([word, freq])

    print('\n' + str(k) + " top most words appear in the writing are: ")
    printKeyValueTable(results)
    return results

def printSimpleList(list):
    '''
    This function is to print all of the items in the list
    Time complexity: O(n)
    Space complexity: O(1)
    Error handling: N/A
    Parameters:
        list (List): Container to print elements from
    Return: N/A
    '''
    for item in list:
        print(item)

def printKeyValueTable(table):
    '''
    This function is to print all of the key value pairs in a given table
    Time complexity: O(n) as it iterates over every list
    Space complexity: O(1)
    Error handling: N/A
    Parameters:
        table (List): Container to print elements from
    Return: N/A
    '''
    for item in table:
        print(str(item[0]) + " : " + str(item[1]))

def main():
    fileName = 'Writing.txt'

    # Task 1
    preprocessedWordList = preprocess(fileName)

    if preprocessedWordList == []:
        print("Unable to continue:")
        print("1. Writing.txt is empty or")
        print("2. There is no word remaining after preprocessing.")
        return

    print("Words are preprocessed")
    response = str(input('Do I need to display the remaining words: '))
    if response == "Y":
        printSimpleList(preprocessedWordList)

    sortedList = wordSort(preprocessedWordList)

    # Task 2
    print("\nThe remaining words are sorted in alphabetical order")
    response = str(input('Do you want to see: '))
    if response == "Y":
        printSimpleList(sortedList)

    # Task 3
    wordCountTable = wordCount(sortedList)
    freqTable = wordCountTable[1:]

    # Task 4
    try:
        kVal = int(input("\nHow many top-most frequent words do I display: "))

        if kVal < 0:
            raise IndexError
    except:
        print("Invalid option given. Printing all results")
        kVal = len(freqTable)

    kTopWordList = kTopWords(kVal,freqTable)

if __name__ == '__main__':
    main()