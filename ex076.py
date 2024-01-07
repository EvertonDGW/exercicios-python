"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

#        0   1   2   3
# Inicializa uma lista com os valores 10, 20, 30 e 40
lista = [10, 20, 30, 40]

# Adiciona a string 'Luiz' ao final da lista
lista.append('Luiz')  
# Agora, a lista é [10, 20, 30, 40, 'Luiz']

# Remove e retorna o último elemento da lista (que é 'Luiz') e armazena em 'nome'
nome = lista.pop()  
# Agora, a lista é [10, 20, 30, 40], e 'nome' contém 'Luiz'

# Adiciona o número 1233 ao final da lista
lista.append(1233)  
# Agora, a lista é [10, 20, 30, 40, 1233]

# Remove o último elemento da lista (que é 1233) utilizando del
del lista[-1]  
# Agora, a lista é [10, 20, 30, 40]

# Insere o valor 5 no índice 100 da lista (a lista é expandida para acomodar este índice)
lista.insert(100, 5)  
# A lista é expandida para incluir espaços intermediários (preenchidos com 0s) até o índice 100.
# Agora, a lista é [10, 20, 30, 40, 0, 0, ..., 5]

# Imprime o valor no índice 4 da lista (que é 5 neste momento)
print(lista[4])  
# Resultado da impressão: 5