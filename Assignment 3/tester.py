from trie import *

def testQuery(filename,id_prefix,last_name_prefix,true_result):
    try:
        test_result = query(filename,id_prefix,last_name_prefix)
    except:
        return ['CRASHED',[]]
    else:
        for i in range(len(test_result)):
            test_result[i] = int(test_result[i])
        test_result = sorted(test_result)
        try:
            assert len(test_result) == len(true_result)
        except AssertionError:
            return ['FAILED',[]]
        else:
            temp = []
            for i in range(len(true_result)):
                try:
                    assert test_result[i] == true_result[i]
                except AssertionError:
                    temp.append(true_result[i])
            if not temp:
                return ['PASSED',[]]
            else:
                return ['FAILED',temp]

def testReverseSubstrings(filename,true_result):
    try:
        test_result = reverseSubstrings(filename)
    except:
        return ['CRASHED',[]]
    else:
        try:
            assert len(test_result) == len(true_result)
        except AssertionError:
            return ['FAILED',[]]
        else:
            temp = []
            for i in range(len(true_result)):
                matched = False
                for j in range(len(test_result)):
                    if test_result[j] == true_result[i]:
                        matched = True
                if not matched:
                    temp.append(true_result[i])
            if not temp:
                return ['PASSED',[]]
            else:
                return ['FAILED',temp]

def trueRead(filename):
    file = open(filename)
    string = file.read().split('TEXT')
    #print(string)
    for i in range(1,len(string)):
        string[i] = string[i].split('\n')
    return string
        
def trueReadTask1(filename):
    string = trueRead(filename)
    for i in range(len(string)):
        temp = []
        for j in range(len(string[i])):
            if string[i][j] != '':
                temp.append(int(string[i][j]))
        string[i] = sorted(temp)
    return (string[1:])

def trueReadTask2(filename):
    string = trueRead(filename)
    for i in range(len(string)):
        temp = []
        for j in range(len(string[i])):
            if string[i][j] != '':
                x = string[i][j].split(' ')
                temp.append([x[0],int(x[1])])
        string[i] = temp
    return (string[1:])
    return string

def testTask1():
    true_result = trueReadTask1('Task-1_text.txt')
    id_prefix = ['123','284','92','50','16801']
    last_name_prefix = ['Wil','Ne','D','Ri','Edw']

    for i in range(5):
        result = testQuery('Database.txt',id_prefix[i],last_name_prefix[i],true_result[i])
        string = ''
        if result[1]:
            string += '\nNOT FOUND INDICES : '
            for j in range(len(result[1])):
                string += str(result[1][j])+' '
        print('TEST CASE -',i+1,': id_prefix :',id_prefix[i],'last_name_prefix :',last_name_prefix[i],'\nOUTCOME :',result[0],string)

def testTask2():
    true_result = trueReadTask2('Task-2_text.txt')
    #print(true_result)

    filename = ['T2_S1.txt','T2_S2.txt','T2_S3.txt','T2_S4.txt','T2_S5.txt']
    for i in range(5):
        result = testReverseSubstrings(filename[i],true_result[i])
        string = ''
        if result[1]:
            string += '\nNOT FOUND ITEMS : '
            for j in range(len(result[1])):
                string += str(result[1][j])+' '
        original = open(filename[i]).read()
        print('TEST CASE -',i+1,' :',original,'\nOUTCOME :',result[0],string)

if __name__ == '__main__':
    testTask1()
    testTask2()
    
        
    
