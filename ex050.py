"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco) # a porcetagem (%) é usada como tag format, s significa strin,f significa float/ponto flutuante
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500))  # %x(minusculo) ou %X(maiusculo) transforma para hexadecimal. o numero 08 vai preencher com 0 ate completar 8 casas hexadecimais

# a porcetagem que esta na cor rosa, é o que permiti essa formatação/interpolação