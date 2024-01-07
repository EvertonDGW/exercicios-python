# Definindo uma string com 5 caracteres
string = 'ABCDE'  # Aqui, a variável 'string' recebe a sequência de caracteres 'ABCDE'.

# Criando uma lista com diferentes tipos de elementos
lista = [123, True, 'Luiz Otávio', 1.2, []]    # uma lista e definida por colchetes ---> [ ]
# Aqui, a variável 'lista' é criada como uma lista que contém um inteiro, um booleano, uma string,
# um número de ponto flutuante e uma lista vazia como elementos.

# Modificando o terceiro elemento da lista para 'Maria'
lista[-3] = 'Maria'
# Aqui, o terceiro elemento da lista (índice -3) é alterado para a string 'Maria'.
# O índice -3 corresponde ao terceiro elemento contando do final para o início.

# Imprimindo a lista modificada
print(lista)
# Aqui, a lista é impressa após a modificação. Deve exibir o resultado com 'Maria' no lugar de 'Luiz Otávio'.

# Imprimindo o terceiro elemento da lista e seu tipo
print(lista[2], type(lista[2]))
# Aqui, o terceiro elemento da lista é impresso (que agora é 'Maria') junto com seu tipo.
# A saída esperada é 'Maria' e <class 'str'>, indicando que o terceiro elemento é uma string.