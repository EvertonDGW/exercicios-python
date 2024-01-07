"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
# Cria uma lista chamada lista_a com elementos de diferentes tipos.
lista_a = ['Luiz', 'Maria', 1, True, 1.2]

# Faz uma cópia da lista_a e atribui à lista_b.
lista_b = lista_a.copy()

# Modifica o primeiro elemento da lista_a.
lista_a[0] = 'Qualquer coisa'

# Imprime a lista_a após a modificação.
print(lista_a)

# Imprime a lista_b, que deve permanecer inalterada.
print(lista_b)