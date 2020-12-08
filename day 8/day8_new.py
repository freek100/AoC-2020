# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 11:45:48 2020

@author: freek
"""

def readAndFormat(filename):
    data= open(filename, 'r').read().split('\n')
    for line in data:
        data[data.index(line)]=line.split()
    return data

def runInstruction(ins):
    accum=0
    index=0
    check=set()
    while True:
        if index in check:
            completed=0
            break
        check.add(index)
        if index>len(ins)-1:
            completed=1
            break
        opcode= ins[index][0]
        if opcode=='acc':
            accum+=int(ins[index][1])
            index+=1
        elif opcode=='jmp':
            index+=int(ins[index][1])
        elif opcode=='nop':
            index+=1
    return accum,completed

def checkFix(ins):
    for ii in range(len(ins)):
        copy=ins[:]
        accum=0
        complete=0
        if copy[ii][0]=='nop':
            ori=copy[ii][0] 
            copy[ii][0]='jmp'
            #print(f'For index: {ii}, change {ori} to {copy[ii][0]}') #Om te checken of hij de verandering goed doet
            accum, complete= runInstruction(copy)           
        elif copy[ii][0]=='jmp':
            ori=copy[ii][0] 
            copy[ii][0]='nop'
            #print(f'For index: {ii}, change {ori} to {copy[ii][0]}') #Om te checken of hij de verandering goed doet
            accum, complete= runInstruction(copy)
        if complete==1:
            print(f'Corrected rule for completion: {ii}')
            acc_fix=accum
    return acc_fix  
     
def main():
    instructions= readAndFormat('day8.txt')
    print(f'Part 1) Accumulator= {runInstruction(instructions)[0]}')
    print(f'Part 2) Accumulator= {checkFix(instructions)}')
    
main()
    
    