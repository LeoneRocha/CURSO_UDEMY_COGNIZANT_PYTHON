import os
#print (os.getcwd())

pastacorrente = os.getcwd()

unsorted_file_name ="animals.txt"
sorted_file_name =  "animals-sorted.txt"

pasta_unsorted_file_name  = pastacorrente+ "\\FILES\\" + unsorted_file_name
pasta_sorted_file_name    = pastacorrente+ "\\FILES\\" + sorted_file_name

animals = []
try:
    with open(pasta_unsorted_file_name) as animals_file:
        print('LENDO {0}.'.format(unsorted_file_name))
        for line in animals_file:
            animals.append(line) 
        print('LEU {0}.'.format(unsorted_file_name))
except:
    print('FALHA AO ABRIR {0}.'.format(unsorted_file_name))

animals.sort()
try:
    with open(pasta_sorted_file_name, 'w') as animals_sorted_file:
        for animal in animals:
            animals_sorted_file.write(animal)
        print('GRAVOU {0}.'.format(sorted_file_name))    
except:
    print('FALHA AO ABRIR {}.'.format(sorted_file_name))