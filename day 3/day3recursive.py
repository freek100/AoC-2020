# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 08:31:05 2020

@author: freek
"""
import pandas as pd

def readData():
    return pd.read_csv('day3.txt', header=None)[0].tolist()

def reducedColumn(width,column):
    if column>width-1:
        column=column-width
        column=reducedColumn(width,column)
    return column

def collisionCounter(forest,stepCol,stepRow):
    collisions=0
    width=len(forest[0])
    Nrows=round(len(forest)/stepRow)
    for i in range(Nrows):
        row= stepRow*i    
        col= stepCol*i
        col= reducedColumn(width,col)
        if forest[row][col]=='#':
            collisions+=1
    return collisions
        
def main():
    forest=readData()
    slope_2= collisionCounter(forest,3,1)
    print('Part 1) '+ str(slope_2) + ' trees encountered')
    multiply= slope_2*collisionCounter(forest,1,1)*collisionCounter(forest,5,1)*collisionCounter(forest,7,1)*collisionCounter(forest,1,2)
    print('Part 2) '+ str(multiply))
    
main()
