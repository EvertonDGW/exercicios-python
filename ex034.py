distancia = float(input('qual a ditancia da sua viagem? '))
print('voce esta preste a começar uma vieagem de {} km'.format(distancia))
if distancia <= 200:
    preço = distancia*0.50
else:
    preço = distancia*0.45
print('e o preço da sua passagem sera de R${:.2f}'.format(preço))
