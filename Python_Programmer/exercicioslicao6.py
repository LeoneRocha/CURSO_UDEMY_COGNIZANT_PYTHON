from logging import exception

def getResultado(estudante ,pontuacao):
    pontosPossibilidade = 100
    porcentagem = round(int(pontuacao) / pontosPossibilidade, 2)
    print(porcentagem)
   # resultado ="erro"    
    if 1>= porcentagem >=0.9:
        resultado = "A"
    elif 0.9 >= porcentagem >=0.8:
        resultado = "B"
    elif 0.8 >= porcentagem >=0.7:
        resultado = "C"
    elif 0.7 >= porcentagem >=0.6:
        resultado = "C" 
    elif 0.6 >= porcentagem >=0.5:
        resultado = "D"   
    elif 0.5 >= porcentagem >=0.4:
        resultado = "E"
    elif 0.4 >= porcentagem >=0.3:
        resultado = "F"  
    else:
        resultado = "h"            

    print("Percentual é {}".format(porcentagem))
    print("A: {} -N: {}".format(estudante, resultado))   

try:
    
    estudante = input("Digite seu nome:")
    pontuacao =int(input("DIgite sua pontuacao:"))
     
    getResultado(estudante, pontuacao)
except Exception:
    print("Digitar numero valido" )