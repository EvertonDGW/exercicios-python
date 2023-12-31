dias=int(input('quantos dias alugados?  '))
km=float(input('quantos km rodados?  '))
pago= (dias * 60) + (km * 0.15)   #a diaria custa 60 reais  .  0.15 centavos por km rodado
print('o total a pagar e de R${:.2f}'.format(pago))
