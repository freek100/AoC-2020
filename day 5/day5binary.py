# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 14:13:31 2020

@author: freek
"""

def readAndFormatData(filename):
    data= open(filename, 'r').read().split('\n')
    for line in data:
        data[data.index(line)]=[line[:7],line[7:]]
    return data

def dec2binary(line,one,zero):
    line=line.replace(one,'1').replace(zero,'0')
    result=0; base= 0 #Initializing values
    for val in line[::-1]:
        result+= int(val)*2**base
        base+=1
    return result

def seatID(passes):
    seatIDs=[0]*len(passes)
    for line in passes:
        seatIDs[passes.index(line)]=8*dec2binary(line[0],'F','B')+dec2binary(line[1],'R','L')
    return seatIDs

def checkMissingID(seatIDs):
    checklist= list(range(min(seatIDs)+8,max(seatIDs)-8)) #Plus and minus 8 as we're not on the first or last row
    return list(set(checklist)-set(seatIDs))[0]

def main():
    passes= readAndFormatData('day5.txt')
    seatIDs= seatID(passes)
    print(f'Part 1) Highest seat ID is {max(seatIDs)}')
    print(f'Part 2) Your seat ID is {checkMissingID(seatIDs)}')
    
main()