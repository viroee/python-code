fra = str(input('Digite uma frase ? ')).upper() .strip()
print('A letra A aparece {} vezes na frase.'.format(fra.count('A')))
print('A Primera letra A apareceu na posição {}'.format(fra.find('A')+1)) #adicionando +1 começa contando 1
print('Onde aparece a ultima letra A na frase {}'.format(fra.rfind('A')))

