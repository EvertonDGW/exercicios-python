""" while/else """
string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == '':  # o break so sera executado se a confição for verdadeira, que não o caso ja que letra e diferente de vazio ''
        break

    print(letra)
    i += 1
else:
    print('Não encontrei um espaço na string.')
print('Fora do while.')
