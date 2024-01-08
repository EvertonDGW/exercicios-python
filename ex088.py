salas = [
    # 0        1
    ['Maria', 'Helena', ],  # lista 0
    # 0
    ['Elaine', ], #lista 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  #lista 2

    #sim ate as listas tem indice,ou seja, ali temos a lista 0, 1 e 2
]   

#print(salas[1][0])  # Imprime 'Elaine' . o primeiro numero e referente a numeração da lista, o segundo numero é o indice do elemento
#print(salas[0][1])  # Imprime 'Helena'   o primeiro numero e referente a numeração da lista, o segundo numero é o indice do elemento
#print(salas[2][2])  # Imprime 'Eduarda'    o primeiro numero e referente a numeração da lista, o segundo numero é o indice do elemento


for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)