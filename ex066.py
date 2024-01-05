""" Calculadora com while """
while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None #Essa variável será usada para verificar se os números inseridos pelo usuário são válidos

    num_1_float = 0
    num_2_float = 0

    #try ... except: Tenta converter as entradas numero_1 e numero_2 para números de ponto flutuante usando float(). Se a conversão for bem-sucedida, a variável numeros_validos é definida como True. Se houver uma exceção (erro), numeros_validos permanece como None.
    
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
        sexcept:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue
 
    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:  #len vai ler a a quantidade/comprimento dos caracteres
        print('Digite apenas um operador.')
        continue

    print('realizanod sua conta,resultado abaixo')

            if operador == '+':
        print(f'{num_1_float} + {num_2_float} = ' num_1_float + num_2_float)

    elif operador == '-':
       print(f'{num_1_float} + {num_2_float} = ' num_1_float - num_2_float)

    elif operador == '/':
        print(f'{num_1_float} + {num_2_float} = ' num_1_float * num_2_float)

    elif operador == '*':
        print(f'{num_1_float} + {num_2_float} = ' num_1_float / num_2_float)
    else:
        print('nunca devia chegar aqui')

    # O método lower() é chamado para garantir que a entrada seja convertida para minúsculas
    # startswith('s') verifica se a entrada começa com 's'.

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
