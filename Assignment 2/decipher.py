class Decipher:
    def __init__(self):
        self.message = ""

    def messageFind(self, inputFileName):
        '''
        This function finds the longest common sub-sequence of two texts based on the file's content, basically
        decrypting our message

        Time Complexity: O(nm) where n is the size of the first text and m is the size of the second text
        Space Complexity: O(nm)
        Error handle:
            - Returns if no input file is given
        Cases covered:
            - One line empty
            - Both lines empty
            - Both lines not matching
            - Start and end of both lines are matching
            - Start and end of both lines are not
            - Variable lengths
            - One line being a subset of the other
        Parameter:
            - inputFileName: String containing the file name of the encrypted words
        Return:
            - None
        Pre-requisite:
            - File contains two lines, with each line containing a String
        '''
        if len(inputFileName) == 0:
            return

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
        DP = [[None for i in range(numOfCols)] for j in range(numOfRows)]

        # Fill every element in the table based on recurrence relation
        for i in range(numOfRows):
            for j in range(numOfCols):
                if i == 0 or j == 0:
                    DP[i][j] = 0
                elif firstWord[i-1] == secondWord[j-1]:
                    DP[i][j] = 1 + DP[i-1][j-1]
                else:
                    DP[i][j] = max(DP[i-1][j], DP[i][j-1])

        # Message retrieval
        # Begin at bottom-right most element and iterate backwards until word is generated
        rowPos = numOfRows - 1
        colPos = numOfCols - 1

        while rowPos > 0 and colPos > 0:
            if (DP[rowPos-1][colPos] == DP[rowPos][colPos-1]) and (DP[rowPos-1][colPos] != DP[rowPos][colPos]):
                # Element above and element up have the same values AND they're different to current element
                # Add to string and move up diagonally
                self.message = firstWord[rowPos-1] + self.message
                rowPos -= 1
                colPos -= 1
            elif DP[rowPos-1][colPos] > DP[rowPos][colPos - 1]:
                # Element above is higher in value than element at left => Move up
                rowPos -= 1
            else:
                # Move left
                colPos -= 1

    def wordInDict(self, dictList, word):
        '''
        Returns the position of a given word (index + 1) if a word is found in the dictionary

        Time Complexity: O(n) where n is the size of the dictionary
        Space Complexity: O(1)
        Error handle: None
        Parameter:
            - dictList : List of words to check for
            - word : String of word to find in dictionary
        Return:
            - Position of word in dictionary (index + 1)
            - (-1) otherwise
        Pre-requisite: N/A
        '''
        for i in range(len(dictList)):
            if word == dictList[i]:
                location = i + 1
                return location
        return -1

    def largestWordInList(self, list):
        '''
        This function finds the largest word in the list

        Time Complexity: O(n) where n is the size of the list
        Space Complexity: O(1)
        Error handle: None
        Parameter:
            list : The list to find the largest String
        Return:
            String of the largest String
        Pre-requisite: List is not empty
        '''
        largestWord = list[0]

        for word in list:
            if len(word) > len(largestWord):
                largestWord = word

        return largestWord

    def wordBreak(self, dictionaryFileName):
        '''
        This function separates the decrypted message into multiple words based on a given dictionary.

        Time Complexity: O(kM . NM)
        Space Complexity: O(kM + NM)
        Error handle:
            - Early return if dictionary file name is not given
            - Early return if dictionary contents is empty
        Cases covered:
            - Use of large words
            - Two words in dictionary together
            - Multiple words in dict together
            - Empty dictionary
            - No matching words
            - Start of word isn't a word
            - End of word isn't a word
            - Word smaller than largest dict word
        Parameter:
            - dictionaryFileName: String of the file name for the dictionary
        Return:
            - None
        Pre-requisite:
            - self.message containing the decrypted message
        '''

        # Early exit if dictionary file name is not given
        if len(dictionaryFileName) == 0:
            return

        # Get the words from the dictionary file and place into a list
        dictFile = open(dictionaryFileName)
        dictContent = []
        for line in dictFile:
            line = line.strip()
            if (len(line) > 0) and (len(line) < len(self.message)) :
                dictContent.append(line)
        dictFile.close()

        # If dictionary file is empty
        if len(dictContent) == 0:
            return

        # Get the largest word, its length will be used as part of the number of rows
        largestWord = self.largestWordInList(dictContent)
        numOfRows = 1 + len(largestWord)

        # Make DP table based prev values
        numOfCols = len(self.message) + 1
        DP = [[0 for i in range(numOfCols)] for j in range(numOfRows)]

        # Loop over every row and col
        for i in range(numOfRows):
            for j in range(numOfCols):
                # Base case
                if i == 0 or j == 0 :
                    DP[i][j] = 0
                    continue

                # See if the last i elements form a word which is in the dictionary
                location = self.wordInDict(dictContent, self.message[j-i: j])

                if location != -1:
                    # Jackpot: Fill in the last i elements with the index of the word
                    for k in range(j, j-i, -1):
                        DP[i][k] = location
                else:
                    # Word from last i elements do not fit the dictionary
                    DP[i][j] = DP[i-1][j]

        # Get results from the last row
        output = ""
        lastRow = DP[-1][1:]

        lastNumber = lastRow[0]
        wordLength = 0

        for i in range(0, len(lastRow)):
            # If the numbers differ OR the current word being built exceeds its limit -> Add a space and reset
            if (lastRow[i] != lastNumber) or (lastNumber != 0 and (wordLength >= len(dictContent[lastNumber - 1]))):
                output += " "
                lastNumber = lastRow[i]
                wordLength = 0
            output += self.message[i]
            wordLength += 1

        # Set class variable 'message' to output
        self.message = output

    def getMessage(self):
        return self.message

def main():
    # Get files
    encryptedFile = str(input("The name of the file, contains two encrypted texts : "))
    dictFile = str(input('The name of the dictionary file : '))
    print("---------------------------------------------------------------------")

    # Do operations
    decipher = Decipher()

    # Find the encrypted message
    decipher.messageFind(encryptedFile)
    print("Deciphered message is " + decipher.getMessage())

    # Break the encrypted message into words
    decipher.wordBreak(dictFile)
    print("True message is " + decipher.getMessage())
    print("---------------------------------------------------------------------")

    print("Program end")

if __name__ == '__main__':
    main()
