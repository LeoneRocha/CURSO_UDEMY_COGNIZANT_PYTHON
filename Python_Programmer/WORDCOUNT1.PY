import os 
import operator
import sys

argumentos = ""
#sys.argv[1]
arquivoNomeFull = "shake.txt"

def removepunct(string):
  punctstr = ".,-,#,>,<,{,},[,],(,),=,==,*,?,0,1,2,3,4,5,6,7,8,9,+,/,:,'"
  nopunctstr = ""
  for letter in string:
    if letter.lower() not in punctstr:
      nopunctstr += letter.lower()
  return nopunctstr

#print(pasta_arquivo)
try: 
    if  argumentos != "":
        arquivoNomeFull = argumentos 

    arquivoNomePartes =arquivoNomeFull.split(".") 
    arquivoNome = arquivoNomePartes[0]
    arquivoNOmeExtensao = arquivoNomePartes[1]
    
    pastacorrente = os.getcwd()   
    pasta_arquivo  = pastacorrente+ "\\Python_Programmer\\" + arquivoNomeFull
    arquivoNomeOrdenado = arquivoNome + "-count-."+ arquivoNOmeExtensao
    pasta_arquivoOrdenado  = pastacorrente+ "\\Python_Programmer\\" + arquivoNomeOrdenado

    arquivo = open(pasta_arquivo,'r')
    texto = removepunct( arquivo.read().lower())
    palavras = {}
    palavrasEncontradas = texto.split()
 
    for palavra in palavrasEncontradas:
        if palavra in palavras:
            palavras[palavra] += 1
        else: 
            palavras[palavra] = 1

    palavrasOrdenada = sorted(palavras.items(), key=operator.itemgetter(1), reverse=True)
    #print(palavrasOrdenada)
    arquivoOrdenado = open(pasta_arquivoOrdenado,'w')
    arquivoOrdenado.write("Total Words: "+ str(len(palavrasEncontradas))+"\n")
    #str(sum(palavrasOrdenada.values()))+"\n")
    arquivoOrdenado.write("Distinct Words: "+ str(len(palavrasOrdenada))+"\n"+"\n")
    #str(len(palavrasOrdenada.keys()))+"\n")
    for chave,valor in palavrasOrdenada: 
        arquivoOrdenado.write("{} - {}\n".format(chave,valor))

    arquivoOrdenado.close()

except (FileNotFoundError):
        print("File is being created to Write:")
      
#finally:
       