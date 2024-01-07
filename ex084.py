"""
enumerate - enumera iteráveis (índices)
"""
# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

for indice, nome in enumerate(lista): #enumerate é utilizada para enumerar as iterações, ou seja, ele vai atribuir indice aos elementos
    print(indice, nome, lista[indice])

    #indice: Armazena o índice do elemento atual na iteração.
    #A variável nome armazena os elementos (valores) da lista durante cada iteração do loop.
    #lista[indice] vai exibir os elementos correspondente ao seu indice

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)


# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')