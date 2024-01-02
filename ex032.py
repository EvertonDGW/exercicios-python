from random import randint
from time import sleep

computador = randint(0, 5)  # Vai pensar em um número aleatório entre 0 e 5
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))  # O jogador tenta adivinhar
print('Processando...')
sleep(3)  # Vai esperar 3 segundos para mostrar o resto do código abaixo

if jogador == computador:
    print('Parabéns, você acertou!')
else:
    print('Você errou. Eu pensei no número {} e não no número {}'.format(
        computador, jogador))
