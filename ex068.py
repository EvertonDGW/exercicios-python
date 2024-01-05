frase = 'aaaooo'

# Inicializa o índice do loop
i = 0

# Inicializa variáveis para rastrear a letra que apareceu mais vezes e a quantidade de vezes que ela apareceu
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

# Loop enquanto o índice é menor que o comprimento da string
while i < len(frase):
    # Obtém o caractere atual
    letra_atual = frase[i]

    # Verifica se o caractere atual é um espaço em branco e, se sim, passa para o próximo caractere
    if letra_atual == ' ':
        i += 1
        continue

    # Conta quantas vezes o caractere atual aparece na string
    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

    # Verifica se o caractere atual apareceu mais vezes do que o anteriormente mais frequente
    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        # Atualiza a letra e a quantidade de vezes
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual

    # Avança para o próximo caractere
    i += 1

# Imprime o resultado
print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)