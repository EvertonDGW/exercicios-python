salario = float(input('Qual é o salário do funcionário? R$'))

if salario <= 1250:
    novo = salario + (salario * 15/100)  # 15 porcento
else:
    novo = salario + (salario * 10/100)  # 10 porcento

print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salario, novo))