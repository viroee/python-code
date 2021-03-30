'''co = float(input('comprimmento do cateto oposto :'))
ca = float(input('Comprimemnto do cateto adjacente:'))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))'''
#import math
from math import hypot
co = float(input('comprimmento do cateto oposto :'))
ca = float(input('Comprimemnto do cateto adjacente:'))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))