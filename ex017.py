salario=float(input('qual é o salario do funcionario? R$  '))
novo=salario+(salario *15/100) # o numero 15 representa um aumento de 15%. primeiro é feito a divisão de 15/100
print('um funcionario que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario,novo))

# codigo para dar aumento no salario de funcionario