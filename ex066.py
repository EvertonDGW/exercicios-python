"""Calculadora com while"""

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None

    num_1_float = 0
    num_2_float = 0

    # try...except para tentar converter os números fornecidos pelo usuário (numero_1 e numero_2) em números de ponto flutuante (float). Se a conversão for bem-sucedida, a variável numeros_validos é definida como True. Se ocorrer uma exceção (por exemplo, se o usuário inserir algo que não pode ser convertido para float), a variável numeros_validos permanecerá como None.

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    print('Realizando sua conta, resultado abaixo:')

    if operador == '+':
        print(f'{num_1_float} + {num_2_float} = {num_1_float + num_2_float}')

    elif operador == '-':
        print(f'{num_1_float} - {num_2_float} = {num_1_float - num_2_float}')

    elif operador == '/':
        if num_2_float != 0:  # Adicionei uma verificação para evitar divisão por zero
            print(f'{num_1_float} / {num_2_float} = {num_1_float / num_2_float}')
        else:
            print('Não é possível dividir por zero.')
    elif operador == '*':
        print(f'{num_1_float} * {num_2_float} = {num_1_float * num_2_float}')
    else:
        print('Operador inválido.')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair:
        break