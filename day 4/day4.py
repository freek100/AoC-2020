# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 08:43:48 2020

@author: freek
"""
import re

def readAndFormatData(filename):
    data= open(filename, 'r').read().split('\n\n')
    i_line=-1
    for line in data:
        i_line+=1
        data[i_line]= line.replace('\n',' ').split()
    return data
        
def checkValidIndex(data):
    valid_i= []
    for line in data:
        if len(line)==8:
            valid_i.append(data.index(line))
        elif len(line)==7:
            cat_valid=True
            for cat in line:
                if 'cid' in cat:
                    cat_valid=False
            if cat_valid==True:
                valid_i.append(data.index(line))
    return valid_i
                    
def checkValid2(data,valid_i):
    valid_passports=0
    for i in valid_i:
        valid_passport= True
        passport= data[i]
        for cat in passport:
            field=cat.split(':')[0]
            var= cat.split(':')[1]
            if checkCategory(field,var) == False:
                valid_passport= False
        if valid_passport==True:
            valid_passports+=1
    return valid_passports
                
def checkCategory(category,variable):
    validCat=False
    if category=='byr':        
        if 1920<=int(variable)<=2002:
            validCat=True
    elif category=='iyr':
        if 2010<=int(variable)<=2020:
            validCat=True
    elif category=='eyr':
        if 2020<=int(variable)<=2030:
            validCat=True
    elif category=='hgt':
        length= int(re.split(r'(\d+)', variable)[1])
        system= re.split(r'(\d+)', variable)[2]
        if system=='cm' and 150<=length<=193:
            validCat=True
        elif system=='in' and 59<=length<=76:
            validCat=True
    elif category=='hcl':
        if variable[0]=='#' and len(variable)==7:
            validCat=True
    elif category=='ecl':
        if variable in ['amb','blu','brn','gry','grn','hzl','oth']:
            validCat=True
    elif category=='pid':
        if len(variable)==9:
            validCat=True
    elif category=='cid':
        validCat=True
    return validCat

def main():
    passports=readAndFormatData('day4.txt')
    valid_i= checkValidIndex(passports)
    print(f'Part 1) {len(valid_i)} passports valid')
    valid2=checkValid2(passports,valid_i)
    print(f'Part 2) {valid2} passports valid')
    
main()