# Atribui a string 'Maria Helena' à variável nome
nome = 'Maria Helena'  

# Inicializa a variável índice com o valor 0
indice = 0

# Inicializa a variável novo_nome com a string 'everton'
novo_nome = 'everton'

# Enquanto o índice for menor que o comprimento da string nome
while indice < len(nome): # esse ciclo se repete enquanto a condição for verdadeira
    # Obtém o caractere na posição do índice na string nome
    letra = nome[indice]

    # Concatena o caractere precedido por um asterisco à string novo_nome
    novo_nome += f'*{letra}'

    # Incrementa o índice para avançar para o próximo caractere na próxima iteração
    indice += 1

# Adiciona um asterisco ao final da string novo_nome
novo_nome += '*'

# Imprime a nova string resultante
print(novo_nome)