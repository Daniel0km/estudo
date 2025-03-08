d1 = 1/20
d2 = 1/10
d3 = 15/100
d4 = 1/5

pp = float(input("Valor do produto: "))
dp = str(input("O produto vai ter desconto? sim ou não "))
if dp == "sim":
    vd = float(input("Quanto vai ser o desconto? 5%, 10%, 15%, 20%(0 para escolher o valor do desconto): "))
    if vd == 5:
        print("o valor do produto de {} ira ser de {}".format(pp, pp-(pp*d1)))
    elif vd == 10:
        print("o valor do produto de {} ira ser de {}".format(pp, pp-(pp*d2)))
    elif vd == 15:
        print("o valor do produto de {} ira ser de {}".format(pp, pp-(pp*d3)))
    elif vd == 20:
        print("o valor do produto de {} ira ser de {}".format(pp, pp-(pp*d4)))
    elif vd == 0:
        pvd = int(input("Qual o valor do desconto? "))
        nd = pvd/100
        print("o valor do produto de {} ira ser de {}".format(pp, pp-(pp*nd)))
else:
    print("Tudo bem vai ser o valor cheio de {}".format(pp))