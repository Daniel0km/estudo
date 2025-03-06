m = float(input("quanto dinheiro você tem na carteira? R$ "))
d = str(input("você quer converter para Euro ou Dolar? "))
dolar = m / 5.7558
euro = m / 6.2131

if d == "Dolar":
    print("com {}R$ você pode comprar {} dolares".format(m, dolar))
elif d == "Euro":
    print("com {}R$ você pode comprar {} euros".format(m, euro))
else:
    print("Moeda estrangeira inválida")