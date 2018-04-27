#Problems from https://www.hackerrank.com/contests/pythonist3/challenges

import string,re
from itertools import groupby,combinations


##################################################
#https://www.hackerrank.com/contests/pythonist3/challenges/capitalize

def capitalize(sentence):
    return ' '.join([word.capitalize() for word in sentence.split(" ")])

##################################################
#https://www.hackerrank.com/contests/pythonist3/challenges/alphabet-rangoli

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

##################################################
#https://www.hackerrank.com/contests/pythonist3/challenges/ginorts

def ginorts():
    string_to_sort = input()
    num=[]
    low=[]
    upp=[]
    for i in string_to_sort:
        if i.islower():
                low.append(i)
        elif i.isupper():
                upp.append(i)
        else:
            num.append(i)
    low.sort()
    upp.sort()
    num.sort()
    num.sort(key=lambda x: True if int(x)%2==0 else False)
    sorted_string = ''.join(low+upp+num)
    print(sorted_string)

##################################################
#https://www.hackerrank.com/contests/pythonist3/challenges/compress-the-string

def compress_the_string():
    input_string=input()
    grp = [(len(list(g)),int(k)) for k,g in groupby(input_string)]
    print(*grp)

##################################################
#https://www.hackerrank.com/contests/pythonist3/challenges/iterables-and-iterators

def iterables_and_iterators():
    n = input()
    letters = input().split(" ")
    k = int(input())

    all_combinations = list(combinations(''.join(map(str,letters)), k))
    allowed_combinations = [i for i in all_combinations if 'a' in i]

    print(len(allowed_combinations)/len(all_combinations))

##################################################
#https://www.hackerrank.com/contests/pythonist3/challenges/validating-credit-card-number

def validate(n):
    #To check if digit
    all_digits = re.findall(r'\d',n)
    a = True if len(all_digits) == 16 else False
    #To check if 4 digits in group
    b = True if len(re.findall(r'(\d{4})',n)) == 4 else False
    #To check if starts with 4,5,6
    c = True if re.findall(r'^[456]',n) else False
    #To check if only - and digits can be used
    non_digits = len(re.findall(r'[^\d]',n))
    d = True if non_digits in [0,3] else False
    #To check consecutive digits
    grps = set([len(list(g)) for k,g in groupby(''.join(map(str,all_digits)))])
    e = True if len(grps.difference({1,2,3})) == 0 else False

    result = "Invalid" if False in [a,b,c,d,e] else "Valid"
    print(result)

def validate_credit_cards():
    n = input()
    for i in range(int(n)):
        validate(input())
