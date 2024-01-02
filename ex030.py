nome = str(input('Digite seu nome completo: ')).strip()  # não vai levar em consideração os espaços vazios
print('Analisando seu nome...')
print('Seu nome em maiúsculo é {}'.format(nome.upper()))  # maiúsculo
print('Seu nome em minúsculo é {}'.format(nome.lower()))  # minúsculo
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))  #  - nome.count(' '))) desconsiderando espaços