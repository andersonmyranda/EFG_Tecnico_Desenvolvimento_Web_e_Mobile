import random
import time

computador = random.randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5, tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em qual número eu pensei? '))
print('Processando...')
time.sleep(3)
if jogador == computador:
    print('Parabéns, você acertou, eu pensei exatamente no número {}.'.format(jogador))
elif jogador > 5:
    print('O número tem que ser de 0 a 5 e vc digitou o n° {}.'.format(jogador))
else:
    print(f'Eu pensei no n° {computador} e não no n° {jogador}, você errou...kkkkkkk!!!!')