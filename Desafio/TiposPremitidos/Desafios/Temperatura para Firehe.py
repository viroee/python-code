temp = float(input(' Informe a temperatura CELCIUS :'))
#f = ((9 * temp) / 5) + 32           ordem de precedencia
f = 9 * temp / 5 + 32
print('A temperatura em {}C corresponde em fareheit {}'.format(temp, f))