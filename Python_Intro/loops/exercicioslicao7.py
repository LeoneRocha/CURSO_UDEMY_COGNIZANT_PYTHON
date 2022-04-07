
listaTarefas = ['lavar','passar','arrumar','cozinhar']

finalizado = False

while not finalizado:
    entradaTarefa = input('Insira uma tarefa extra para sua lista de tarefas. Pressione <enter> quando terminar:')
    if len(entradaTarefa) == 0:
        finalizado = True
    else:
        listaTarefas.append(entradaTarefa)
        print('Tarefa adicionada.')
# Display the to-do list.
    
print()
print('Voce tem num total de {0} tarefas.'.format(len(listaTarefas)))
#slice
segundaTarefa = listaTarefas[1:2]
print()
print('a Segunda tarefa é {0}'.format(segundaTarefa) )

ultima = listaTarefas[-1]
print()
print('a ultima tarefa é {0}'.format(ultima) )

print()
print('Sua lista de tarefas:')
print('-' * 50)
print()
for tarefa in listaTarefas:
    print(tarefa)

print()
print('Sua lista de tarefas ordenada:')
print('-' * 50)

listaTarefasOrdenada = sorted (listaTarefas) 

for tarefaO in listaTarefasOrdenada:
    print(tarefaO.upper())
 
def buscarTarefa ():
    busca = input('DIgite a tarefa que deseja buscar:')
    if len(busca) == 0:
       print('Busca Cancelada.')
    else:   
        resultbusca = verSeTemATarefa(busca)
        print(resultbusca)
        
         
def verSeTemATarefa(nome):
    """Get tarefa por ordem.""" 
    try:
        busca_index = listaTarefas.index(nome)
        resultado = "a tarefa {0} ta na posicao {1}".format( listaTarefas[busca_index].upper(), busca_index)
        return resultado
    except:
        resultado = 'Tarefa não encontrada.'
    return resultado

buscarTarefa ()


print()
print('as 2 primeiras sao :')
for number in range(0, len(listaTarefas), 2):
    print(listaTarefas[number].upper())
