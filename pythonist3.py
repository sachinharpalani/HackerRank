#Problems from https://www.hackerrank.com/contests/pythonist3/challenges


##################################################
#https://www.hackerrank.com/contests/pythonist3/challenges/capitalize

def capitalize(sentence):
    return ' '.join([word.capitalize() for word in sentence.split(" ")])

##################################################
#https://www.hackerrank.com/contests/pythonist3/challenges/alphabet-rangoli

import string

def alphabet_rangoli(size):
    alphabets=(string.ascii_lowercase[:size])[::-1]
    for i in range(size*2-1):
        for j in range(abs(size-1-i)):
            print('--',end='')
        if i < size:
            k = alphabets[:i+1] + ((alphabets[:i+1])[::-1])[1:]
        else:
            k = alphabets[:size-i-1] + ((alphabets[:size-i-1])[::-1])[1:]
        for j in range(len(k)):
            print(k[j],end='')
            if j < len(k)-1:
                print('-',end='')
        for j in range(abs(size-1-i)):
            print('--',end='')
        print()
