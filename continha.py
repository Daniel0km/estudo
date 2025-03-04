class Conta:
    def __init__(self, titular, numero, saldo):
        self.saldo = 0  
        self.numero = numero
        self.titular = titular 

    def setsaldo(self, saldo):
        if saldo<0:
            print("Saldo não pode ficar abaixo e 0")
        else:
            self.saldo = saldo

