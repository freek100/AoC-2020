# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 09:01:47 2020

@author: freek
"""

def readAndFormat(filename):
    data= open(filename, 'r').read().split('.\n')
    for i in range(len(data)):
        data[i]=data[i].split(', ')
        data[i][0]=data[i][0].split(' contain ')
        data[i].append(data[i][0][1])
        data[i][0]=data[i][0][0]
        for j in range(len(data[i])):
            if ' bags' in data[i][j]:
                data[i][j]= data[i][j].replace(' bags','')
            else:
                data[i][j]= data[i][j].replace(' bag','')
            if j>0:
                data[i][j]=data[i][j].split(' ',1)
    colorlist=[]
    for color in data:
        colorlist.append(color[0])
    return data, colorlist
    
def checkShinyGold(color,bags,colorlist):
    if color not in colorlist:
        return 0
    index= colorlist.index(color)
    gold=0
    for subbags in bags[index][1:]:
        if gold==0:
            if 'shiny gold' in subbags[1]:
                gold=1
            elif 'other' in subbags[1]:
                gold=0
            else:
                gold=checkShinyGold(subbags[1],bags,colorlist)
    return gold
    
def countBags(color,bags,colorlist):
    bagsinside=0
    if color not in colorlist:
        return bagsinside
    index= colorlist.index(color)
    for subbags in bags[index][1:]:
        if 'other' in subbags[1]:
            bagsinside=0
        else:
            bagsinside+=int(subbags[0])+int(subbags[0])*countBags(subbags[1],bags,colorlist)
    return bagsinside
 
def main():           
    bags, colorlist=readAndFormat('day7.txt')
    shinyGold= [0]*len(bags)
    for color in colorlist:
        shinyGold[colorlist.index(color)]=checkShinyGold(color,bags,colorlist)   
    print(f'Part 1) {sum(shinyGold)} bags')
    print(f'Part 2) {countBags("shiny gold",bags,colorlist)} bags inside a single shiny gold bag')

main()
