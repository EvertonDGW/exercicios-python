# importamos a biblioteca math,mas seleionando unicamente o componente sqrt, usado para calcular raiz quadrada
from math import sqrt   #a o lado de sqrt podemos colocar a propriedade floor ou ceil assim --> sqrt,floor ou sqrt,ceil
num = int(input('digite um numero:  '))
raiz = sqrt(num) 
print('a raiz de {} é igual a {}'.format(num,raiz)) 