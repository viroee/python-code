'''tempo = int(input('Quantos anos tem seu carro: '))
if tempo <=4:
    print('Carro novo')
else:
    print('Carro velhor')
print('--FIM--')'''
tempo = int(input('Quantos anos tem seu carro: '))
print('Carro novo ' if tempo <=3 else 'Carro velho')
print('--FIM--')