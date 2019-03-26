def normalInsertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] <= key:
            array[j+1] = array[j]
            j = j - 1
        array[j+1] = key

if __name__ == '__main__':
    arr = [1,4,2,1,5]
    normalInsertionSort(arr)
    print(arr)