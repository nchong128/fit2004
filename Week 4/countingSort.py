import random, time

def countingSort(list):
    # Works with non-negative integers only btw

    if len(list) == 1:
        return list

    # Find the largest element
    largestElem = list[0]
    for i in range(1, len(list)):
        if list[i] > largestElem:
            largestElem = list[i]

    # Create list from 0...largestElem + 1
    count = [0 for i in range(largestElem + 1)]

    # Increment count based on elem
    for elem in list:
        count[elem] += 1

    # Go across count and append to sortedList
    sortedList = []

    for i in range(len(count)):
        for j in range(count[i]):
            sortedList.append(i)

    return sortedList

def sample(numOfLists, listSize):
    result = []

    for i in range(numOfLists):
        result.append(random.sample(range(100),listSize))

    return result

def main():
    ### SMALL SAMPLE
    smallSample = sample(numOfLists = 1000, listSize = 10)

    smallTimeStart = time.time()
    # Do counting sort for small samples
    for list in smallSample:
        countingSort(list)

    smallTimeEnd = time.time()
    smallTimeElapsed = smallTimeEnd - smallTimeStart

    # Print time
    print(str(smallTimeElapsed) + "s")

    ### LARGE SAMPLE
    largeSample = sample(numOfLists = 1000, listSize = 1000)

    largeTimeStart = time.time()
    # Do counting sort for large samples
    for list in largeSample:
        countingSort(list)

    largeTimeEnd = time.time()
    largeTimeElapsed = largeTimeEnd - largeTimeStart

    # Print time
    print(str(smallTimeElapsed) + "s")


if __name__ == "__main__":
    main()

'''
Problem 2
=============
a) Select the first element of the sequence
- Element is chosen at random
- Worst case is O(n^2) where n is the length of the list
- Example case: Where the first element is either the smallest or the largest of the list

b) Select the minimum element of the sequence
- Minimum element so it will partition every element to one list,
  the other list being empty
- O(n^2) where n is the length of the list
- Example case: Any list

c) Select the median element of the sequence
- O(n^2) even with quick select algorithm
- Example case: 

d) Select an element that is greater than exactly 10% of the others
- O(n^2) as even with the median it will be O(n^2)
- Example case: 

'''