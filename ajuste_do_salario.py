#dados do funcionario
n = str(input("Nome do empregado: "))
sa = float(input("De quanto é o salario atual de {}? ".format(n)))

r = str(input("O reajuste será para aumentar ou diminuir? "))
#aumentar
if r == "aumentar":
    ra = int(input("de quanto será o aumento? "))
    rda = ra/100
    print("O salario de {} qua era de {} agora será de {}".format(n, sa, sa+(sa*rda)))
    f = str(input("Tem certesa? sim ou não "))
    if f == "sim":
        print("Salario aumentado")
    else:
        print("O salario de {} continuara o mesmo, sendo {}".format(n, sa))
#diminuir
if r == "diminuir":
    rd = int(input("De quanto será a diminuição? "))
    rdd = rd/100
    print("O salario de {} que antes era de {} agora será de {}".format(n, sa, sa-(sa*rdd)))
    f = str(input("Tem certesa? sim ou não "))
    if f == "sim":
        print("Salario diminuido")
    else:
        print("O salario de {} continuara o mesmo, sendo {}".format(n, sa))