import time
import os
class Cronometro:
    def __init__(self, mseg = 0, seg = 0, mim = 0, hs = 0, d = 0):
        self.milisegundos = mseg
        self.segundo = seg
        self.minuto = mim
        self.horas = hs
        self.dia = d

    def __repr__(self):
        return f'{self.dia:02d}:{self.horas:02d}:{self.minuto:02d}:{self.segundo:02d}:{self.milisegundos:02d}'
    
    def incremento(self):
        self.milisegundos += 1
        if self.milisegundos >= 60:
            self.milisegundos = 0
            self.segundo += 1
        if self.segundo >= 60:
            self.segundo = 0
            self.minuto += 1
        if self.minuto >= 60:
            self.minuto = 0
            self.horas += 1
        if self.horas >= 24:
            self.horas = 0
            self.dia +=1
    
    def start(self):
        while True:
            os.system('cls')
            print(self)
            self.incremento()
    time.sleep(1)


cornometro1 = Cronometro()
cornometro1.start()