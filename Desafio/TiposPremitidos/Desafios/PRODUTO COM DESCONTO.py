preço = float(input('Qual é o preço do produto ? R$'))
novo = preço - (preço * 5 / 100)
print('o preço do seu produto de {}, agora com desconto de 5% custará R${}'.format(preço, novo))