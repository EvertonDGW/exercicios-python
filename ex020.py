import math  #importamos a biblioteca math
num = int(input('digite um numero:  '))
raiz = math.sqrt(num) #sqrt é uma tag da biblioteca math que server para calcular a raiz quadrada de um numero
print('a raiz de {} é igual a {}'.format(num, math.ceil (raiz)))   #a tag ceil do math vai arredonda o resultado da raiz quadrada pra cima
                                                                # no lugar de ceil voce pode colocar floor para arredondar para baixo
