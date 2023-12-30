preço=float(input('qual é o preço do produto? R$ '))
novo=preço - (preço * 5/100) #o numero 5 representa o desconto (%) em relação ao preço. primeiro e feito a divisão de 5/100. 
print('o produto que custava R${:.2f}, na promoção com desconto de 5% vai custa R${:.2f}'.format(preço,novo))

#codigo para dar desconto em algum produto
