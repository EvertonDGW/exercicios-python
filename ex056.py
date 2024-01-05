# Programa para verificar se um número é par ou ímpar:
entrada = input("Digite um número inteiro: ")

try:
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar' if not par_impar else 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')
except ValueError:
    print('Você não digitou um número inteiro')

# Programa para exibir saudação com base na hora:
hora = int(input("Digite a hora (0-23): "))

if 0 <= hora <= 11:
    print('Bom dia!')
elif 12 <= hora <= 17:
    print('Boa tarde!')
elif 18 <= hora <= 23:
    print('Boa noite!')
else:
    print('Hora inválida. Digite um valor entre 0 e 23.')

# Programa para verificar o comprimento do nome:
nome = input("Digite seu primeiro nome: ")

if len(nome) <= 4:   #len vai ler a quantidade de caracteres
    print('Seu nome é curto.')
elif 5 <= len(nome) <= 6:
    print('Seu nome é normal.')
else:
    print('Seu nome é muito grande.')