nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome <= 1:
    print('Digite mais de uma letra.')
elif 1 < tamanho_nome <= 4:
    print('Seu nome é curto')
elif 5 <= tamanho_nome <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')