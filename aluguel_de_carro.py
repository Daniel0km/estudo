#tempo com o carro
t = int(input("Quanto dais você ficou com o carro? "))
km = float(input("quantos kilometros você percorreu? "))


print("Por ter ficado {} dias com o carro irá pagar {} e por ter percorrido {}km deva pagar {}. Assim você pagará {}".format(t, t*60, km, km*0.15, (t*60)+(km*0.15)))