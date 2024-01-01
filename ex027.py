import random
n1=str(input('primeiro aluno: '))
n2=str(input('segundo aluno: '))   #str significa string
n3=str(input('terceiro aluno: '))
n4=str(input('quarto aluno: '))
lista=[n1,n2,n3,n4]
random.shuffle(lista) #shuffle vai embaralhar a ordem da lista
print('a ordem de apresentação sera')
print(lista)