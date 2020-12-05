# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 09:34:50 2020

@author: freek
"""

def readAndFormatData(filename):
    data= open(filename, 'r').read().split('\n')
    for line in data:
        fb= line[:7]
        rl= line[7:]
        data[data.index(line)]=[fb,rl]
    return data

def getRow(row_ins):
    row= list(range(128))
    for letter in row_ins:
        if letter=='F':
            row= row[:int((len(row)/2))]
        if letter=='B':
            row= row[int((len(row)/2)):]
    return row[0]

def getCol(col_ins):
    col= list(range(8))
    for letter in col_ins:
        if letter=='L':
            col=col[:int(len(col)/2)]
        if letter=='R':
            col=col[int(len(col)/2):]
    return col[0]

def getSeats(Bpasses):
    seat_reg=list(range(len(Bpasses)))
    for Bpass in Bpasses:
        seat=[0,0]
        seat[0]= getRow(Bpass[0])
        seat[1]= getCol(Bpass[1])
        seat_reg[Bpasses.index(Bpass)]=seat 
    return seat_reg

def getSeatID(seat_reg):
    seat_IDs= list(range(len(seat_reg)))
    for seat in seat_reg:
        seat_IDs[seat_reg.index(seat)]=seat[0]*8+seat[1]
    return seat_IDs

def checkMissingSeat(seat_IDs):
    seat_IDs.sort()
    for seat in seat_IDs[1:(len(seat_IDs)-1)]:
        if seat-1 != seat_IDs[seat_IDs.index(seat)-1]:
            missing_seat= seat-1
    return missing_seat
    
def main():
    Bpasses= readAndFormatData('day5.txt')
    seats= getSeats(Bpasses)
    seat_ID= getSeatID(seats)
    print(f'Part 1) Maximum seat ID is {max(seat_ID)}')
    print(f'Part 2) Your seat is {checkMissingSeat(seat_ID)}')
    
main()


