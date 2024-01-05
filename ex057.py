entrada = input('Digite um número: ')

if entrada.isdigit(): #A função isdigit() verifica se todos os caracteres na string são dígitos (0 a 9). Se você digitar uma letra ou qualquer caractere não numérico, a função isdigit() retornará False,
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'par' if par_impar else 'ímpar'

    print(f'O número {entrada_int} é {par_impar_texto}')
else:
    print('Você não digitou um número inteiro')

try:
    entrada_float = float(entrada)
    par_impar_float = entrada_float % 2 == 0
    par_impar_texto_float = 'par' if par_impar_float else 'ímpar'

    print(f'O número {entrada_float} é {par_impar_texto_float}')
except ValueError:
    print('Você não digitou um número válido')