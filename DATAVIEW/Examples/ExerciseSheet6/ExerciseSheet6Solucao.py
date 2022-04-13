
import matplotlib.pyplot as plt
import datetime as  datahora
from mpl_toolkits.mplot3d import Axes3D as gph3D
 
#carrotData = readCSV(pasta_arquivo + "carrotPrices.csv")
#onionData = readCSV(pasta_arquivo + "onionPrices.csv") 

def lerTxt (fileName):
    f = open(fileName,"r")
    data = {}
    
    for line in f:
        part1 = line.strip("\n").split(" ")
        dataName = part1[0]
        restData = part1[1:]

        finalData = []
    if dataName == "date": 
        for dataString in restData:
            tempDate = [int(i) for i in dataString.split("-")]
            finalData.append(datahora.date(tempDate[0],tempDate[1],tempDate[2]))
    elif dataName == "price":
        finalData = [float(i) for i in restData]
        data[dataName] = finalData

        for x in restData:
            finalData.append(int(x))
            
        data[dataName] = finalData
        
    f.close()
    return data


def readCSV(fileName):
    f = open(fileName,"r")  
    data = {}
    
    firstLine = f.readline().strip("\n").split(",")[1:]

    for name in firstLine:
        data[name] = []    
    
    for line in f:
        processedLine = line.strip("\n").split(",")[1:]
        
        tempDate = [int(i) for i in processedLine[0].split("-")]

#        tempDate = processedLine[0].split("-")
#        for i in range(len(tempDate)):
#            tempDate[i] = int(tempDate[i])
#        print(tempDate)

        tempDT = datahora.date(tempDate[0],tempDate[1],tempDate[2])
        
        price = float(processedLine[1])
        
        data["date"].append(tempDT)
        data["price"].append(price)
#        print(data)
#        break
        
        
    return data

import os
pastacorrente = os.getcwd()   
pasta_arquivo  = pastacorrente+ "\\DATAVIEW\\Examples\\Sheet5E1Solution\\" 

carrotData = readCSV(pasta_arquivo + "carrotPrices.csv")
onionData = readCSV(pasta_arquivo + "onionPrices.csv") 

