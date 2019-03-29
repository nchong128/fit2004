import os
from decipher import *

class test_cipher:
    def __init__(self):
        self.test = ''
        self.true = ''
        
    def test_messageFind(self,f1,f2):
        result = 'PASSED'
        crashed = False
        try:
            cipher = Decipher()
            cipher.messageFind(f1)
            self.test = cipher.getMessage()
        except:
            crashed = True
            result = 'CRASHED'

        fin = open(f2)
        self.true = fin.read()
        fin.close()

        if not crashed:
            try:
                assert self.true == self.test
            except AssertionError:
                result = 'FAILED'
                print('TRUE ANSWER : '+self.true)
                print('YOUR ANSWER : '+self.test)
        return result

    def test_wordBreak(self,f1,f2):
        result = 'PASSED'
        crashed = False
        try:
            cipher = Decipher()
            cipher.message = self.true
            cipher.wordBreak(f1)
            self.test = cipher.getMessage()
        except:
            crashed = True
            result = 'CRASHED'

        fin = open(f2)
        self.true = fin.read()
        fin.close()

        if not crashed:
            try:
                assert self.true == self.test
            except AssertionError:
                result = 'FAILED'
                print('TRUE ANSWER : '+self.true)
                print('YOUR ANSWER : '+self.test)
        return result

if __name__ == '__main__':
    tc = test_cipher()
    print('='*50)
    print('Test cases'+' '*(20-len('Test cases'))+'Task-1'+' '*(10-len('Task-1'))+'Task-2'+' '*(10-len('Test-2'))+'Final')
    print('-'*50)
    for i in range(1,6):
        result = ['','']
        f_encrypt = os.getcwd() + '\Input\encrypted_' + str(i) + '.txt'
        f_dictionary = os.getcwd() + '\Input\dictionary_' + str(i) + '.txt'
        f_true_1 = os.getcwd() + '\Input\E_' + str(i) + '.txt'
        f_true_2 = os.getcwd() + '\Input\W_' + str(i) + '.txt'
        result[0] = tc.test_messageFind(f_encrypt,f_true_1)
        result[1] = tc.test_wordBreak(f_dictionary,f_true_2)
        string = 'Test : '+str(i)+' '*(20-len('Test : '+str(i)))+result[0]+' '*(10-len(result[0]))+result[1]+' '*(10-len(result[1]))
        if result[0] == 'PASSED' and result[1] == 'PASSED':
            string += 'PASSED'
        else:
            string += 'FAILED'
        print(string)
        print('-'*50)
        
