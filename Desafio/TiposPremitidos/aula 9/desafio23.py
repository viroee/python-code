''''n1 = int(input('Informe um número: '))
num = str(n1)
print('Analisando numero {}'.format(n1))
print('Unidade: {}'.format(num[3]))
print('Dezena: {}'.format(num[2]))
print('Centena: {}'.format(num[1]))
print('Milhar: {}'.format(num[0]))'''''

num = int(input('Informe um número: '))
un = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando numero {}'.format(num))
print('Unidade: {}'.format(un))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
