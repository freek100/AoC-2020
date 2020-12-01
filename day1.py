# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 14:53:50 2020

@author: freek
"""

import csv

data=open('day1.csv')
ex_report = list(csv.reader(data))

#Puzzle part 1
for i in range(len(ex_report)-1):
    var1= int((ex_report[i])[0]) #Die tweede index is omdat hij anders var1 opslaat als list, en niet als getal
    for j in range(i+1,len(ex_report)):
        var2= int((ex_report[j])[0])
        if var1+var2==2020:
            puzzle_answer1= var1*var2
            
print(puzzle_answer1)

#Puzzle part 2
for i in range(len(ex_report)-2):
    var1= int((ex_report[i])[0])
    for j in range(i+1,len(ex_report)-1):
        var2= int((ex_report[j])[0])
        for k in range(j+1,len(ex_report)):
            var3= int((ex_report[k])[0])
            if var1+var2+var3==2020:
                puzzle_answer2= var1*var2*var3

print(puzzle_answer2)
    