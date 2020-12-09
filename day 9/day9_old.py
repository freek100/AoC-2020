# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 09:31:46 2020

@author: freek
"""
from random import shuffle

def readData(filename):
    data= open(filename, 'r').read().split('\n')
    for x in data:
        data[data.index(x)]=int(x)
    return data

def runSums(numbers,preamb_len):
    preamb= list(range(1,preamb_len+1))
    checknum= preamb[:]
    shuffle(checknum)
    for num in numbers:
        if checkSum(num,checknum)==True:
           checknum.append(num)
           checknum.pop(0)
        else:
            notsum= num
            break
    return notsum
      
def checkSum(number, checklist): #Check if number is a sum of 
    valid=False
    for i in range(len(checklist)-1):
        for j in range(i,len(checklist)):
            if checklist[i]+checklist[j]==number:
                valid=True
    return valid

def contSum(target,numbers):
    for i in range(len(numbers)):
        j=i
        sumval= numbers[i]
        while sumval<=target:
            j+=1
            sumval+=numbers[j]
            if sumval==target:
                contset= numbers[i:j+1]
    return min(contset)+max(contset)
 
def main():   
    numlist= readData('day9.txt')
    p1= runSums(numlist,25)
    print(f'Part 1) {p1}')
    print(f'Part 2) {contSum(p1,numlist)}')
    
main()
