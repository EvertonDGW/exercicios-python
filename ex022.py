import math
num=float(input('digite um numero com virgula:  ')) 
print('o valor digitado foi {} e a parte inteira é {}'.format(num, math.trunc(num) )) # no lugar de math.trunc voce pode colocar -> int(num)
