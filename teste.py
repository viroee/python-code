import random
n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceciro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = (n1, n2, n3, n4)
escolhido = random.choice(lista)
print('O Aluno escolhido foi {}:'.format(escolhido))




