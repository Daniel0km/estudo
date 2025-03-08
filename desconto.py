d1 = 0,10 - 0,5
d2 = 0,1
d3 = 0,15
d4 = 0,20

pp = float(input("Valor do produto: "))
dp = str(input("O produto vai ter desconto? sim ou não "))
if dp == "sim":
    vd = float(input("Quanto vai ser o desconto? 5%, 10%, 15%, 20%: "))
    if vd == 5:
        print("o valor do produto de {} ira ser de {}".format(pp, pp-d1))
    elif vd == 10:
        print("o valor do produto de {} ira ser de {}".format(pp, pp-d2))
    elif vd == 15:
        print("o valor do produto de {} ira ser de {}".format(pp, pp-(pp*d3)))
    elif vd == 20:
        print("o valor do produto de {} ira ser de {}".format(pp, pp-(pp*d4)))
else:
    print("Tudo bem vai ser o valor cheio de {}".format(pp))