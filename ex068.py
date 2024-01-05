frase = 'aaaaooo'

# Inicialização de variáveis
i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

# Loop while para percorrer a string
while i < len(frase):
    letra_atual = frase[i]

    # Ignora espaços em branco
    if letra_atual == ' ': # esse comanod nao necessariamente necessario, ele so esta caso houver espaçoes em brancos dentro da variavel frase
        i += 1
        continue

    # Conta quantas vezes a letra atual aparece na string
    qtd_atual = frase.count(letra_atual)

    # Verifica se a letra atual apareceu mais vezes que a letra anteriormente mais frequente
    if qtd_apareceu_mais_vezes <= qtd_atual:
        qtd_apareceu_mais_vezes = qtd_atual
        letra_apareceu_mais_vezes = letra_atual

    # Incremento do contador para passar para o próximo caractere
    i += 1

# Imprime o resultado
print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)