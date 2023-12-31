import math  #importamos a biblioteca math
num = int(input('digite um numero:  '))
raiz = math.sqrt(num) #sqrt é uma tag da biblioteca math que server para calcular a raiz quadrada de um numero
print('a raiz de {} é igual a {}'.format(num, math.ceil (raiz)))   #a tag ceil do math vai arredonda a raiz quadrada pra cima
