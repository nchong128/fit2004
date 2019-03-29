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
        file = open(inputFileName)
        firstWord = file.readline().strip()
        secondWord = file.readline()
        file.close()

        # Get lengths of words
        firstLen = len(firstWord)
        secondLen = len(secondWord)

        # Early exit of words are the same
        if firstWord == secondWord:
            self.message = firstWord

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

    def wordBreak(self, dictionaryFileName):

        pass

    def getMessage(self):
        return self.message

def main():
    inputFile = 'Input/PERSONAL1.txt'
    dictFile = 'Input/dictionary_1.txt'

    test = Decipher()

    test.messageFind(inputFile)

    print(test.getMessage())

if __name__ == '__main__':
    main()
