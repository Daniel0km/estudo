l = float(input("qual é a larqura da sua parede? "))
a = float(input("qual é a altura da sua parede? "))

print("com uma parede {} de largura e {} de autura sua parede tem {}m²".format(l, a, l*a))

p = str(input("você quer pintar sua parede? "))

if p == "sim":
    print("para pintar sua parede você precisa de {} litros de tinta".format((l*a)/2))
else:
    print("tudo bem você não pintar sua parede")