viagem = float(input('Qual a distancia da sua viagem ? '))
print('Você está preste a fazer uma viagem de {}Km'.format(viagem))
if viagem <=200:
    preço = viagem * 0.50
else:
    preço = viagem * 0.45
print('E o preço da sua passagem será de R${}'.format(preço))