dias = float(input('Quantos dias alugados ?'))
km = float(input('Quantos Km Rodados ?'))
custa = dias * 60 # custa = (dias * 60) + (km * 0.15) poderia ser assim tbm
kmr = km * 0.15
print('O Total a pagar é de R${}'.format(custa + kmr))