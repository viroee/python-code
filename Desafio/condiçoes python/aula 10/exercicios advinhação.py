from random import randint
from time import sleep
computador = randint(0, 5) #Faz o computador ''pensar''
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente Adivinhar...')
print('-=-' * 20)
eu = int(input('Qual Numero Eu Pensei? ')) # jogador tenta avidinhar
print('PROCESSANDO...')
sleep(2)
if eu == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}'.format(computador, eu))


