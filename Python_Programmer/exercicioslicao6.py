from codecs import getreader
from unittest import result


pontosPossibilidade = 100
estudante = input("Digite seu nome:")
pontuacao = input("DIgite sua pontuacao:")

porcentagem = round(pontuacao / pontosPossibilidade, 2)
resultado ="erro"

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
    