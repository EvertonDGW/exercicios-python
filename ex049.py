# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5 --> indice/posição onde esta cada letra da palavra otavio. nos numero positivos
#  O t á v i o
# -6-5-4-3-2-1 --> indice/posição onde esta cada letra da palavra otavio. nos numero negativos
# nome = 'Otávio'
# print(nome[2])     usamos esse simbolo --> [] para selecionar o indice que queremos alterar
# print(nome[-4])
# print('vio' in nome)
# print('zero' in nome)
# print(10 * '-')
# print('vio' not in nome)
# print('zero' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')

    # in -> significa 'estar entre'
    # not in -> significa nao estar entre