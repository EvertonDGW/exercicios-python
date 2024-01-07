"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

#        0   1   2   3   4   5
# Cria uma lista com os valores 10, 20, 30 e 40
lista = [10, 20, 30, 40]

# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])

# Adiciona o valor 50 ao final da lista
lista.append(50)

# Remove o último elemento da lista (que é 50 neste momento)
lista.pop()

# Adiciona os valores 60 e 70 ao final da lista
lista.append(60)
lista.append(70)

# Remove o elemento no índice 3 da lista (que é 40 neste momento) e armazena em 'ultimo_valor'
ultimo_valor = lista.pop(3)

# Imprime a lista atualizada, seguida pela mensagem 'Removido,' e o valor que foi removido anteriormente (40)
print(lista, 'Removido,', ultimo_valor)