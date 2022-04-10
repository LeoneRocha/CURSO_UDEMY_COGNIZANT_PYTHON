import math
import os 
import operator
import sys
from turtle import color
import matplotlib.pyplot as plt

pastacorrente = os.getcwd()   
pasta_arquivo  = pastacorrente+ "\\DATAVIEW\\" + "Goals.txt"
#print(pasta_arquivo)
with open(pasta_arquivo, "r") as goalData:
    homeTeamLine = goalData.readline()
    homeTeamLine = homeTeamLine.strip(" \n")
    homeTeamLine = homeTeamLine.split(" ")

    HomeTeamGoals = [int(x) for x in homeTeamLine]
    awayTeamLine = goalData.readline()
    awayTeamLine = awayTeamLine.strip(" \n")
    awayTeamLine = awayTeamLine.split(" ")

    AwayTeamGoals = [int(x) for x in awayTeamLine]

#print(HomeTeamGoals)
#print(AwayTeamGoals)
def distFromZero(htg, atg):
    return math.sqrt(htg**2 + atg **2)

colors =[]

for indice in range(len(HomeTeamGoals)):
    colors.append(distFromZero(HomeTeamGoals[indice], AwayTeamGoals[indice] ))


fig = plt.figure("pontinhos", figsize=(10,10))
ax1 = fig.add_subplot(1,1,1)#nrows ncollumns

#print(colors)
plt.scatter(x= HomeTeamGoals, y = AwayTeamGoals, s=100, c=colors)
plt.sca(ax1)
plt.show()