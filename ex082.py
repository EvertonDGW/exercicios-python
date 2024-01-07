# Desempacotamento de variáveis em uma lista ['Maria', 'Helena', 'Luiz']
# O primeiro e segundo elementos são ignorados com underscores (_).
# O terceiro elemento é atribuído à variável 'nome'.
# O restante dos elementos é coletado na lista 'resto' usando o operador *.
_, _, nome, *resto = ['Maria', 'Helena', 'Luiz',]

# Imprime o valor da variável 'nome', que é o terceiro elemento da lista.
print(nome)
print(resto) #Neste caso, como não há mais elementos após 'Luiz', a lista resto permanece vazia. Se você modificar a lista de entrada para incluir mais elementos, você verá esses elementos na lista resto.
