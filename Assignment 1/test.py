def test():
    fileArray = ['oneRepeated.txt','justOneWord.txt', 'sample.txt', 'sample1.txt', 'sample2.txt','punctuationStartEnd.txt']

    for i in range(len(fileArray)):
        fileArray[i] = 'sampleText\\' + fileArray[i]

    fileArray.append('Writing.txt')

    for filename in fileArray:
        input("\nNow running script for filename " + filename)

        w = preprocess(filename)
        print(w)

        x = wordSort(w)
        print(x)

        y = wordCount(x)
        print(y)

        z = kTopWords(k = 5, sortedWithFreqList = y[1:])
        print(z)
