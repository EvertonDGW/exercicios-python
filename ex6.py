n1=int(input('digite um numero:'))
n2=int(input('digite outro numero:'))
s=n1+n2
m=n1*n2
d=n1/n2     # / e o quociente da dvisão
di=n1//n2   #// e o resto da divisão
e=n1**n2
print('a soma e {}\n a multiplicação e {}\n e a divisão e {:.3f}'.format(s, m, d),end='') #{:.3f} -> significa que vai aparecer 3 casas apos a virgula. digite o numero 4 e 3 no terminal
print('a divisão inteira e {} o expoente e {}'.format(di,e))

#  ,end=''  ->  vai fazer com que a linha 8 e 9 sejam exibidas na mesma linha no terminal
# \n -> significa nova linha,ou seja, ela é uma quebra de linha semelhante a tag br do html