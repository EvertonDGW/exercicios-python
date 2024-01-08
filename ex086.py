import decimal  # Importa a biblioteca decimal para aritmética decimal precisa

# Define dois números decimais com precisão
numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')

# Realiza a soma dos dois números decimais
numero_3 = numero_1 + numero_2

# Imprime o resultado da soma
print(numero_3)

# Imprime o resultado da soma com precisão de duas casas decimais usando f-string
print(f'{numero_3:.2f}')

# Imprime o resultado da soma arredondado para duas casas decimais
print(round(numero_3, 2))