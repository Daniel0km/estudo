num = int(input("Por favor escreva um número para a tabuada: "))
'''print('{} * {} = {}'.format(num, 1, num*1))
print('{} * {} = {}'.format(num, 2, num*2))
print('{} * {} = {}'.format(num, 3, num*3))
print('{} * {} = {}'.format(num, 4, num*4))
print('{} * {} = {}'.format(num, 5, num*5))
print('{} * {} = {}'.format(num, 6, num*6))
print('{} * {} = {}'.format(num, 7, num*7))
print('{} * {} = {}'.format(num, 8, num*8))
print('{} * {} = {}'.format(num, 9, num*9))'''
print("_"*15)
for i in range(1, 101):
    print('{} * {:2} = {:4}'.format(num, i, num * i))

print("_"*15)