# senha_salva = '123456'
# senha_digitada = ''
# repeticoes = 0

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha ({repeticoes}x): ')

#     repeticoes += 1

# print(repeticoes)
# print('Aquele laço acima pode ter repetições infinitas')

texto = 'Python'  # Inicializa a variável 'texto' com a string 'Python'
novo_texto = ''   # Inicializa uma nova variável 'novo_texto' como uma string vazia

# Inicia um loop for que itera sobre cada letra na string 'texto'

for letra in texto: # A expressão for letra in texto: pode ser lida da seguinte forma:"Para cada letra na sequência de texto, faça alguma coisa." .os valores armazenados dentro da ariavel texto e guardado dentro da variavel letra para cada iteração

    novo_texto += f'*{letra}'  # Adiciona um asterisco seguido pela letra atual à variável 'novo_texto'
    print(letra)               # Imprime a letra atual durante cada iteração

# Imprime a string resultante, onde cada letra é precedida por um asterisco e a string é seguida por um asterisco no final
print(novo_texto + '*')





