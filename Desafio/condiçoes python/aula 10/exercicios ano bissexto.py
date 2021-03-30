from datetime import date
bissexto = int(input('Que ano voce quer analisar ? coloque um 0 para analisar o ano atual :'))
if bissexto == 0:
    bissexto = date.today().year
if bissexto % 4 == 0 and bissexto % 100 != 0 or bissexto % 400 == 0:
    print('O ano {} é bissexto'.format(bissexto))
else:
    print('O ano {} NÃO é Bissexto'.format(bissexto))

