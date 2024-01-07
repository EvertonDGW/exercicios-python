"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

# Define a palavra que o jogador precisa adivinhar
palavra_secreta = 'perfume'

# Inicializa uma string vazia para armazenar as letras que o jogador acertou
letras_acertadas = ''

# Inicializa um contador para o número de tentativas do jogador
numero_tentativas = 0

# Inicia um loop infinito, o jogo continua até ser interrompido
while True:
    # Solicita ao jogador que digite uma letra
    letra_digitada = input('Digite uma letra: ')

    # Incrementa o contador de tentativas
    numero_tentativas += 1

    # Verifica se o jogador digitou mais de uma letra
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue  # Pula para a próxima iteração do loop

    # Verifica se a letra digitada está presente na palavra secreta

    if letra_digitada in palavra_secreta: #Essa linha verifica se a letra_digitada está presente na palavra_secreta. Se sim, a letra_digitada é considerada uma letra correta e é adicionada à string letras_acertadas. Isso é feito para manter o registro das letras que o jogador já acertou.
    
        letras_acertadas += letra_digitada  # Adiciona a letra às letras acertadas

    # Inicializa uma nova string para representar a palavra oculta com as letras adivinhadas
    palavra_formada = ''
    
    # Itera sobre cada letra na palavra secreta

    for letra_secreta in palavra_secreta: #A variável letra_secreta é uma variável temporária usada no loop for. A cada iteração do loop, ela assume o valor da próxima letra na palavra_secreta

        # Se a letra foi adivinhada, adiciona à palavra_formada, senão, adiciona um asterisco
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta #O comando palavra_formada += letra_secreta é uma maneira concisa de adicionar a letra_secreta à string palavra_formada
        else:
            palavra_formada += '*'

    # Exibe a palavra formada até o momento
    print('Palavra formada:', palavra_formada)

    # Verifica se o jogador adivinhou todas as letras corretamente
    if palavra_formada == palavra_secreta:
        # Imprime mensagem de vitória, exibe a palavra secreta, o número de tentativas
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativas)

        # Reinicia as variáveis para um novo jogo
        letras_acertadas = ''
        numero_tentativas = 0