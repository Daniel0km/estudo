num = int(input("Por favor escreva um número para a tabuada: "))

print("_"*15)
for i in range(1, 101):
    print('{} * {:2} = {:4}'.format(num, i, num * i))

print("_"*15)