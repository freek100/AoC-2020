# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 10:17:40 2020

@author: freek
"""

def readAndFormatData(filename):
    data= open(filename, 'r').read().split('\n\n')
    for line in data:
        data[data.index(line)]= line.replace('\n','-').split('-')
    return data

def anyoneYes(declarations):
    nQuestions=0
    for group in declarations:
        questions=set([])
        for person in group:
            questions=questions|set(person)
        nQuestions+=len(questions)
    return nQuestions

def groupYes(declarations):
    nQuestions=0
    for group in declarations:
        setlist=[]
        for person in group:
            setlist.append(set(person))
        questions= set.intersection(*setlist)
        nQuestions+=len(questions)
    return nQuestions
    
def main():
    declarations= readAndFormatData('day6.txt')
    print(f'Part 1) {anyoneYes(declarations)} questions')
    print(f'Part 2) {groupYes(declarations)} questions')
    
main()