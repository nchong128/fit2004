class PrefixTrie:
    def __init__(self, info, isInt):
        if isInt:
            self.size = 10
        else:
            # A = 0, Z = 25, a = 32, z = 57
            self.size = ord('z') - ord('A') + 1

        self.isInt = isInt
        self.root = self.initialiseArray()

        for entry in info:
            self.insert(entry)

    def initialiseArray(self):
        return PrefixArrayNode(self.size)

    def translateChar(self, char):
        if self.isInt:
            return int(char)
        else:
            return ord(char) - ord('A')

    def insert(self, entry):
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

        # Mark off end
        current.isEnd = True

class PrefixArrayNode:
    def __init__(self, size):
        self.array = [None] * size
        self.isEnd = False

def query(filename, id_prefix, last_name_prefix):
    # Place contents into table and retrieve info
    info = parseInfo(filename)

    # Construct tries based on information
    idTrie = PrefixTrie(info[1], True)
    lastNameTrie = PrefixTrie(info[2], False)

    print("Done")


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

def main():
    filename = 'database.txt'
    query(filename, 'croc', 'sloth')

if __name__ == '__main__':
    main()
