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
- Example case: Where the list is in descending order
    - first element picked will always partition it badly

b) Select the minimum element of the sequence
- Minimum element so it will partition every element to one list,
  the other list being empty
- O(n^2) where n is the length of the list
- Example case: Any list

c) Select the median element of the sequence
- O(n log n) without the quick select algorithm
- Example case: Any list

d) Select an element that is greater than exactly 10% of the others
- O(n log n)
- Example case: Any list

Problem 3
================
- O(n^2) for a a list where the values below/above the mean is only 1 element and the rest of the elements are on the
    other side of the mean

Problem 4
================
- Average case will arise when considering that the green (optimal) part is selected 50% of the time
- If we choose the worst part of the green area, we split the list into 0.75n
- Can keep splitting (i.e. n + 0.75n + 0.75^2 n + ...)
- Bounded by some constant c so n + 0.75n + 0.75^2 n + ... <= c.n
- Hence O(n)

Problem 5
================
- To sort 4329, 5169, 4321, 3369, 2121, 2099
- Sort the numbers from the right to left
- Now sort the last index
- 4321, 2121, 4329, 5169, 3369, 2099
- Sort the second-last index
- 4321, 2121, 4329, 5169, 3369, 2099
- Sort the 3rd-last index
- 2099, 2121, 5169, 4321, 4329, 3369
- Sort the first index
- 2099, 2121, 3369, 4321, 4329, 5169

Problem 6
==============
a) Worst-case: O(nm) where you have to loop through each letter and sort the n words
    - Can be very inefficient if the words are of drastically different sizes so that most of the word would be done in
        adding the padding to the words
b)
- Only apply radix sort to where the letter for a word exists.
- Start from right to left again
- If no letter exists, append to list and sort the remaining

Problem 7
==============
function kClosestToMedian(list, k) 
    n = list.length
    median = quickSelect(list, sum(list) / n)
    
    # Find and keep index of median
    for i = 1...n
        if list[i] == median
            medianPosition = i
            break
        end if
    end for
    
    # Iterate over and convert elements to difference
    for i = 1...n
        if i != medianPosition
            list[i] = list[i] - median
        end if
    end for
    
    # Remove median
    list.remove(medianPosition)
    
    # Find kth order statistic
    kthOrder = quickSelect(list)
    
    # Iterate over each element, if less than the kthOrder, add it to the output
    output = []
    for i = 1...n
        if list[i] > kthOrder
            output.append(list[i])
        end if
    end for
    
    # Add median back to output
    for i = 1...output.length
        output[i] += median
    end for
    
end function

Problem 8
==============
- O(nk) = O(k^2 * n/k)
- n(1/2)^d = k
- d = log(n/k)


'''