"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
is --> significa é
is not --> significa não é
"""
condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')


if passou_no_if is None:  
    print('Não passou no if')
else:
    print('Passou no if')

#---------------------------------------id-------------------------------------------------------
v1= 'A'
v2 ='a'
print(id(v1))
print(id(v2)) # id --> é usado para mostrar o identificador da variavel