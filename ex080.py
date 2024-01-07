"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""

# Cria uma lista chamada lista com elementos do tipo string.
lista = ['Maria', 'Helena', 'Luiz']

# Adiciona um novo elemento 'João' ao final da lista.
lista.append('João')

# Cria uma sequência de índices para a lista.ou seja foi criado uma sequencia de indice para cada elemento
indices = range(len(lista))

# Itera sobre os índices e imprime o índice, o elemento e o tipo do elemento.
for indice in indices:
    print(indice, lista[indice], type(lista[indice]))

    #lista[indice] --> exibirá o elemento da lista que corresponde ao índice atual na iteração do loop.

