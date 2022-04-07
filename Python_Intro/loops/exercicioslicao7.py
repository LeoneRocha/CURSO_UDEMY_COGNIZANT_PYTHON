
litaTarefas = []

finalizado = False

while not finalizado:
    entradaTarefa = input('Insira uma tarefa para sua lista de tarefas. Pressione <enter> quando terminar:')
    if len(entradaTarefa) == 0:
        finalizado = True
    else:
        litaTarefas.append(entradaTarefa)
        print('Tarefa adicionada.')
# Display the to-do list.
    
print()
print('Voce tem num total de {0} tarefas. Sua lista de tarefas:'.format(len(litaTarefas)))
print('-' * 16)

for tarefa in litaTarefas:
    print(tarefa)