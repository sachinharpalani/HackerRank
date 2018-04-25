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

##################################################
#https://www.hackerrank.com/contests/pythonist3/challenges/triangle-quest-2

def triangle_quest():
    for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
        ##This will not work since, str is used which was not allowed
        #print(''.join(map(str,(list(range(1,i+1)[:i+1])+list(range(1,i+1)[::-1])[1:]))))
        #https://www.hackerrank.com/rest/contests/pythonist3/challenges/triangle-quest-2/hackers/praran26/download_solution
        print(((10**i - 1)//9)**2)
