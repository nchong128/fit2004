import os
from roadPath import *

def ansMatched(path,ansTrue):
    error = None
    try:
        assert path[1] == ansTrue[1]
    except AssertionError:
        print('4. User calculated path length :',path[1])
        print('4. True path length :',ansTrue[1])
        error = 4
    else:
        if ansTrue[0]:
            for road in ansTrue[0]:
                if road == path[0]:
                    return None
        else:
            if ansTrue[0] == path[0]:
                return None
        print('5. User found path : ',path[0])
        print('5. True path : ',ansTrue[0])
        error = 5
    return error

def dataTypeMatched(path,ansTrue):
    error = None
    #print(ansTrue)
    if ansTrue[1] == -1:
        try:
            assert type(path) == type([])
        except AssertionError:
            print(ansTrue,path)
            error = 3
        else:
            error = ansMatched(path,ansTrue)
    else:
        try:
            assert type(path) == type(())
        except AssertionError:
            print(ansTrue,path)
            error = 3
        else:
            error = ansMatched(path,ansTrue)
    return error
    
def quickestPathTest(fileGraph,ansTrue,s,t):
    error = None
    try:
        g = Graph()
        g.buildGraph(fileGraph)
    except:
        error = 1
    else:
        try:
            path = g.quickestPath(s,t)
        except:
            error = 2
        else:
            error = dataTypeMatched(path,ansTrue)
    return error

def quickestDetourPathTest(fileGraph,fileService,ansTrue,s,t):
    error = None
    try:
        g = Graph()
        g.buildGraph(fileGraph)
        g.addService(fileService)
    except:
        error = 1
    else:
        try:
            path = g.quickestDetourPath(s,t)
        except:
            error = 2
        else:
            error = dataTypeMatched(path,ansTrue)
    return error

def quickestSafePathTest(fileGraph,fileCamera,fileToll,ansTrue,s,t):
    error = None
    try:
        g = Graph()
        g.buildGraph(fileGraph)
        g.augmentGraph(fileCamera,fileToll)
    except:
        error = 1
    else:
        try:
            path = g.quickestSafePath(s,t)
        except:
            error = 2
        else:
            error = dataTypeMatched(path,ansTrue)
    return error

def trueRead(fileName):
    file = open(fileName)
    s = int(file.readline().replace('\n',''))
    t = int(file.readline().replace('\n',''))
    truePath = [[]]
    trueSafe = [[]]
    trueDetour = [[]]
    tick = -1
    for line in file:
        line = line.replace('\n','')
        #print(line)
        #print(truePath)
        #print(trueSafe)
        #print(trueDetour)
        if line == 'NORMAL':
            tick = 0
        elif line == 'SAFE':
            tick = 1
        elif line == 'DETOUR':
            tick = 2
        else:
            if line != 'None':
                line = line.split()
                if tick == 0:
                    if 'D:' in line[0]:
                        line[0] = line[0].replace('D:','')
                        truePath.append(int(line[0]))
                    else:
                        for i in range(len(line)):
                            line[i] = int(line[i])
                        truePath[0].append(line)
                elif tick == 1:
                    if 'D:' in line[0]:
                        line[0] = line[0].replace('D:','')
                        trueSafe.append(int(line[0]))
                    else:
                        for i in range(len(line)):
                            line[i] = int(line[i])
                        trueSafe[0].append(line)
                elif tick == 2:
                    if 'D:' in line[0]:
                        line[0] = line[0].replace('D:','')
                        trueDetour.append(int(line[0]))
                    else:
                        for i in range(len(line)):
                            line[i] = int(line[i])
                        trueDetour[0].append(line)
    return [s,t,truePath,trueSafe,trueDetour]
                
            

if __name__ == '__main__':
    print('='*130)
    print('Test cases'+' '*(40-len('Test cases'))+'Task-1'+' '*(30-len('Task-1'))+'Task-2'+' '*(30-len('Test-2'))+'Task-3')
    print('-'*130)
    passedScore = 0
    fileGraph = 'basicGraph.txt'
    fileCamera = 'camera.txt'
    fileToll = 'toll.txt'
    fileService = 'service.txt'
    errorType = ['','Graph loading failed','Program crashed','Return type mismatch','Path length incorrect','Path incorrect']
    testType = ['','normal and detour same, but safe','ditto','Shortest path is already safe','Source and sink same','Normal and safe same, but detour','Blocked path','All different','Detour is source','Camera is in source','NO detour and safe','No detour']
    
    for i in range(1,11):
        [s,t,ansTruePath,ansTrueSafe,ansTrueDetour] = trueRead('test-0'+str(i)+'.txt')
        #print('Test-0'+str(i)+'.txt : ',s,t,ansTruePath,ansTrueSafe,ansTrueDetour)
        
        error = quickestPathTest(fileGraph,ansTruePath,s,t)
        #print(error)
        if error is not None:
            string = 'Test:'+testType[i]+' '*(40-len('Test:'+testType[i]))+errorType[error] + ' '*(30-len(errorType[error]))
        else:
            string = 'Test:'+testType[i]+' '*(40-len('Test:'+testType[i]))+'PASSED' + ' '*(30-len('PASSED'))

        error = quickestSafePathTest(fileGraph,fileCamera,fileToll,ansTrueSafe,s,t)
        #print(error)
        if error is not None:
            string += errorType[error] + ' '*(30-len(errorType[error]))
        else:
            string += 'PASSED' + ' '*(30-len('PASSED'))

        error = quickestDetourPathTest(fileGraph,fileService,ansTrueDetour,s,t)
        #print(error)
        if error is not None:
            string += errorType[error] + ' '*(30-len(errorType[error]))
        else:
            string += 'PASSED' + ' '*(30-len('PASSED'))
        print(string)
        print('-'*130)
    print('='*130)
    
