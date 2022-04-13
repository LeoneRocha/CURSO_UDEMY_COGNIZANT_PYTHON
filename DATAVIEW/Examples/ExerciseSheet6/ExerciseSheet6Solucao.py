from re import I
from matplotlib import projections
import matplotlib.pyplot as plt
import datetime as  datahora
from mpl_toolkits.mplot3d import Axes3D as gph3D
from numpy import append
 
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
#load datas
import os
pastacorrente = os.getcwd()   
pasta_arquivo  = pastacorrente+ "\\DATAVIEW\\Examples\\ExerciseSheet6\\" 

carrotData = readCSV(pasta_arquivo + "carrotPrices.csv")
onionData = readCSV(pasta_arquivo + "onionPrices.csv") 

#print(carrotData)
#print(onionData)
#setup 3d plot 
valores  = []
replacement = []

for i in range(len(carrotData["date"])):
    if carrotData["date"][i].day  == 1:
        valores.append(i)
        replacement.append(carrotData["date"][i])

fig = plt.figure(figsize=(8,8))
ax1 = fig.add_subplot(1,1,1,projection="3d")
ax1.set_ylim(0.5,2.5)
ax1.view_init(0,-90)


diasAno  = 365
#print(carrotData["price"])
ax1.plot(xs = [0], ys = [1], zs = carrotData["price"][:1], color= "orange")
ax1.plot(xs = [0], ys = [2], zs = onionData["price"][:1], color= "purple")

for i in range(5,365,5):
    ax1.plot(xs = range(i), ys = [1]* i, zs = carrotData["price"][:i], color= "orange")
    ax1.plot(xs = range(i), ys = [2]* i, zs = onionData["price"][:i], color= "purple")
    ax1.view_init(0+ i/20,-90+1/10)
    plt.draw()
    plt.pause(0.05)
    

#plt.xticks(valores, replacement)

ax1.set_title('Preco de Cebolas e Cenoutras por dias')
#fig.xlabel('Dias')
#fig.ylabel('QUantidade por ano')
ax1.set_ylabel("Preço")
ax1.set_xlabel("Dias")
plt.show()