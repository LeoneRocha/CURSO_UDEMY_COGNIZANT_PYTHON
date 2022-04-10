#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: maxschallwig
"""

#Data Source - http://www.seanlahman.com/baseball-archive/statistics/ 
#Stats for 2017
import os

pastacorrente = os.getcwd()   
pasta_arquivo  = pastacorrente+ "\\DATAVIEW\\readingTheTxtData\\" 


def readTxt():
    f = open(pasta_arquivo+ "Sheet1E1.txt","r")
    data = {}
    
    for line in f:
        part1 = line.strip("\n").split(" ")
        dataName = part1[0]
        restData = part1[1:]

        finalData = []
        for x in restData:
            finalData.append(int(x))
            
        data[dataName] = finalData
        
    f.close()
    return data        
 
txtVersionData = readTxt()
#print(txtVersionData.keys())

for chave in txtVersionData:
    print("{} - {}".format(chave, txtVersionData[chave][:5]))
 


f1 = open(pasta_arquivo+ "Sheet1E1_EXPORT.txt","w")
f1.write(str(txtVersionData))