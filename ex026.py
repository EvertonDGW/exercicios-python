import random
n1=str(input('primeiro aluno: '))
n2=str(input('segundo aluno: '))   #str significa string
n3=str(input('terceiro aluno: '))
n4=str(input('quarto aluno: '))
lista=[n1,n2,n3,n4]
escolhido=random.choice(lista) #choice significa uma escolha,ou seja, ele vai escolhe um dos alunos que estão dentro da lista
print('o aluno esoclhido foi: {}' .format(escolhido))

#sorteando um dos alunos