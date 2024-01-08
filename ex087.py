"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""
# String original com espaços extras e uma vírgula
frase = '   Olha só que   , coisa interessante        ' #perceba que a string é uma só. quando usamos a tag split estamos dividindo a string no meio, a virgula e esse delimitador/marcação,ou seja, temos a string 'olha so que' e 'coisa interessante'

# Divide a string em partes usando a vírgula como delimitador
lista_frases_cruas = frase.split(',')

# Lista para armazenar as partes da frase sem espaços extras
lista_frases = []

# Itera sobre as partes da frase
for i, frase in enumerate(lista_frases_cruas): #enumerate vai enumerar a iteração
    # Adiciona cada parte da frase após remover espaços extras usando o método strip()
    lista_frases.append(lista_frases_cruas[i].strip()) # A função strip() é utilizada para remover espaços em branco e caracteres de quebra de linha do início e do final de uma string.

print(lista_frases_cruas)
print(lista_frases)
   

# Une as partes da frase de volta em uma string usando vírgula e espaço como separadores
frases_unidas = ', '.join(lista_frases) #a função join() tem a função específica de unir os elementos de uma sequência em uma única string.ou seja, join vai unir as partes que foram divididas/separadas

# Imprime a string resultante
print(frases_unidas)




