import random
##sorteando um item de uma lista
'''n1 = str(input('Primeiro item: '))
n2 = str(input('Segundo item: '))
n3 = str(input('Terceiro item: '))
n4 = str(input('Quarto item: '))
lista = [n1, n2, n3, n4]

escolido = random.choice(lista)
print('A ordem de apresentação será: {}'.format(escolido))'''

##sorteando ordem
n1 = str(input('item 1:'))
n2 = str(input('item 2:'))
n3 = str(input('item 3:'))
n4 = str(input('item 4:'))
lista = [n1, n2, n3, n4]

random.shuffle(lista)
print('A ordem de apresentação será: {}'.format(lista))