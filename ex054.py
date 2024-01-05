"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero_str = input(
    'Vou dobrar o número que vc digitar: ' #digite uma letra e voce entendera o try e except
)

try:  # --> vai executar o codigo abaixo
    numero_float = float(numero_str)  
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except: # --> caso alguma linha do codigo dentro de try de erro, o except ira exibir o print abaixo
    print('Isso não é um número')

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número')
    
    