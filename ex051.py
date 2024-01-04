"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a --->  PESQUISE SOBRE ISSO
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}') # 10 significa que vai criar 10 caracteres, a seta indica a direção
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.4873648123746:0=+10,.1f}')  # ---> existem bibliotecas especificas que fazem isso
print(f'O hexadecimal de 1500 é {1500:08X}') #transformando o numero 1500 para hexadecimal . 08 significa que eles vai preencher 8 caracteres com o valor 0
print(f'{variavel!r}')