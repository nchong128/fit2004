'''
- Two texts which encrypt original message with lots of inessential alphabets
- e.g. bdceMlonfashxzunivyeriasityb and MondcaitjshukniveptnQrsiXteyY are two encrypted texts
- contains Monash university
- Looking for longest sequence of common alphabets
- No whitespace in the encrypted texts, none between the alphabets
- Need to find out the words of the deciphered texts
- List of possible words will put the spaces in decipher text to get original message
- First will find the largest subsequence of common alphabets from two encrypted texts ->
    then break the retrieved message into words based on their vocab

- If combination of two or more words of dictionary is another word in the dictionary and present in the message
    e.g. message is IloveMango, in dictionary (an, Man, go, Mango), Going to use Mango
- If dictionary is empty -> Deciphered message will be read as a single word
- If words inside the dictionary do not match -> going to consider the message as a single word

Task 1: Finding the longest subsequence of common alphabets
- Program will decipher the message from two encrypted texts (encrypted.txt)
- function called messageFind
- input size is O(n+m) -> program needs a worst case of O(nm) and space complexity of
    -O(nm)
- Can be upper and lower case only, NO SPACES, NO PUNCTUATIONS
- Consider O(nm + k)

Task 2: Words separating
- Will break deciphered message into multiple words using the vocab, input from dictionary.txt
- Function called wordBreak to break initial deciphered message into multiple words using the dictionary
- Normal condition: break message into available words
- Use of large words: if the combo of two or more words is also another large word -> use the large word
    e.g. 'am',`i',`ice',`cream',`icecream',`is',`old',`cold'and the message is`icecreamiscold',Use`icecream is cold' instead of other patterns
- Empty dictionary : whole message as a single word
- no matching words: while message as a single word
- partially matching words: unmatched segment of message will be treated as separate words

- worst case should be O(kM.NM)
- k is the size of input string
- space complexity is O(kM + NM)

- NOTES
- Size of two texts will not be the same
- input file names may be different
'''
class Decipher:
    def __init__(self):
        self.message = ""

    def messageFind(self, inputFileName):
        # TODO: Deal with edge cases, e.g no input, just one letter, multiple lengths, etc.
        # Retrieve words
        inputFile = open(inputFileName)
        firstWord = inputFile.readline().strip()
        secondWord = inputFile.readline()
        inputFile.close()

        # Get lengths of words
        firstLen = len(firstWord)
        secondLen = len(secondWord)

        # Early exit of words are the same
        if firstWord == secondWord:
            self.message = firstWord
            return

        # Tabulate our results table of (firstLen + 1) rows and (secondLen+1) columns
        numOfRows = firstLen + 1
        numOfCols = secondLen + 1
        memoTable = [[None for i in range(numOfCols)] for j in range(numOfRows)]

        # Fill every element table based on recurrence relation
        for i in range(numOfRows):
            for j in range(numOfCols):
                if i == 0 or j == 0:
                    memoTable[i][j] = 0
                elif firstWord[i-1] == secondWord[j-1]:
                    memoTable[i][j] = 1 + memoTable[i-1][j-1]
                else:
                    memoTable[i][j] = max(memoTable[i-1][j], memoTable[i][j-1])

        ## Message retrieval
        # Begin at bottom-right most element and iterate backwards until word is generated
        rowPos = numOfRows - 1
        colPos = numOfCols - 1

        while rowPos > 0 and colPos > 0:
            if (memoTable[rowPos-1][colPos] == memoTable[rowPos][colPos-1]) and (memoTable[rowPos-1][colPos] != memoTable[rowPos][colPos]):
                # Element above and element up have the same values AND they're different to current element
                # Add to string and move up diagonally
                self.message = firstWord[rowPos-1] + self.message
                rowPos -= 1
                colPos -= 1
            elif memoTable[rowPos-1][colPos] > memoTable[rowPos][colPos - 1]:
                # Element above is higher in value than element at left => Move up
                rowPos -= 1
            else:
                colPos -= 1

    def printTable(self,table):
        for row in table:
            print(row)

    def wordInDict(self, dictList, word):
        # Returns the index of a given word (+ 1) if a word is found in the dictionary
        # -1 otherwise
        location = -1
        for i in range(len(dictList)):
            if word == dictList[i]:
                location = i + 1
                return location
        return -1

    def largestWordInList(self, list):
        largestWord = list[0]

        for word in list:
            if len(word) > len(largestWord):
                largestWord = word

        return largestWord

    def wordBreak(self, dictionaryFileName):
        # Courtesy of Shams
        # TODO: MAKE SURE TO ADJUST THIS FROM 6 TO 0
        # If dictionary file is not given, return
        if len(dictionaryFileName) == 6:
            return

        # Get the words from the dictionary file and place into a list
        dictFile = open(dictionaryFileName)
        dictContent = dictFile.read().split("\n")
        dictFile.close()

        # Filter any empty strings
        filteredDictContent = []
        for entry in dictContent:
            if len(entry) > 0:
                filteredDictContent.append(entry)
        dictContent = filteredDictContent

        if len(dictContent) == 0:
            return

        # Get the largest word, its length will be used as part of the number of rows
        largestWord = self.largestWordInList(dictContent)
        numOfRows = 1 + len(largestWord)

        # Make memoization table based prev values
        numOfCols = len(self.message) + 1
        memoTable = [[0 for i in range(numOfCols)] for j in range(numOfRows)]

        # Loop over every row and col
        for i in range(numOfRows):
            for j in range(numOfCols):
                # Base case
                if i == 0 or j == 0 :
                    memoTable[i][j] = 0
                    continue

                # See if the last i elements form a word which is in the dictionary
                location = self.wordInDict(dictContent, self.message[j-i: j])

                if location != -1:
                    # Jackpot: Fill in the last i elements with the index of the word
                    for k in range(j, j-i, -1 ):
                        memoTable[i][k] = location
                else:
                    # Word from last i elements do not fit the dictionary
                    memoTable[i][j] = memoTable[i-1][j]

        # Iterate over last row and form sentence
        output = ""
        lastRow = memoTable[-1][1:]
        lastNumber = lastRow[0]
        for i in range(0, len(lastRow)):
            if lastRow[i] != lastNumber:
                output += " "
                lastNumber = lastRow[i]
            output += self.message[i]

        # Adjust class variable to output
        self.message = output

    def getMessage(self):
        return self.message

def test():
    inputFile = 'Input/PERSONAL4.txt'
    dictFile = 'Input/EMPTYDICT.txt'

    test = Decipher()

    test.messageFind(inputFile)

    test.wordBreak(dictFile)

    print(test.getMessage())


def main():
    # Get files
    # TODO: MAKE SURE TO REMOVE THE INPUT STRING BELOW AND TO ADJUST THE ERROR CHECKING FOR IT
    encryptedFile = "Input/" + input("The name of the file, contains two encrypted texts: ")
    dictFile = "Input/" + input("The name of the dictionary file: ")
    print("---------------------------------------------------------------------")
    # TODO: MAKE SURE TO REMOVE THE INPUT STRING BELOW AND TO ADJUST THE ERROR CHECKING FOR IT
    # Do operations
    decipher = Decipher()
    decipher.messageFind(encryptedFile)
    print("Deciphered message is " + decipher.getMessage())
    decipher.wordBreak(dictFile)
    print("True message is " + decipher.getMessage())
    print("---------------------------------------------------------------------")
    print("Program end")


if __name__ == '__main__':
    main()
