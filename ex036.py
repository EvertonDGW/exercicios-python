a = int(input('primeiro valor: '))
b = int(input('segundo valor: '))
c = int(input('terceiro valor: '))

# verificando o numero menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

# verificando o numero maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('o menor valor digitado {}'.format(menor))
print('o maior valor digitado {}'.format(maior))
