import RPi.GPIO as GP
from time import sleep
from threading import Thread as thread


# estados --------------------------------------
aberto = 1
cuidado = 0
fechado = -1

# tempos
base = 10

acoes = []

semaforos = []

# temos que entender que como os 2 sensores estao apontando pro semaforo contrario, se passar no sensor, o sinal deve fechar

class Semaforo:
        
    green = 0
    red = 0
    yellow = 0
    
    estado = aberto
    
    def __init__(self, s1, s2, nome):
        self.s1 = s1
        self.s2 = s2
        
        self.nome = nome

        # prepara instancias para os leds

        # coloca os sensores como input
        GP.setup(s1, GP.IN)
        GP.setup(s2, GP.IN)

        # carrega o estado do semaforo

        semaforos.append(self)
        
        thread(None, self.sensores, None, (0, 0)).start()

    # ---------------------------------------

    def Leds(self, red, yellow, green):
        self.red = Cor(red, False, 'red')
        self.yellow = Cor(yellow, False, 'yellow')
        self.green = Cor(green, True, 'green')

    def inicio(self):
        # estado inicial de todos os leds
        self.estado = aberto
        self.red.inicio()
        self.yellow.inicio()
        self.green.inicio()

    def abrir(self):
        self.estado = aberto

        self.green.ligar()
        self.yellow.desligar()
        self.red.desligar()

    def fechar(self, *args, tempo = base):
        self.estado = fechado

        self.green.desligar()
        self.yellow.desligar()
        self.red.ligar()
        
        sleep(tempo)
        
        self.switch()
        
                
    def switch(self):
        if semaforos[not self.nome].estado == cuidado:
           self.abrir()
           semaforos[not self.nome].fechar()
        else:
           self.abrir()
           

    def abrirCuidado(self):
        self.estado = cuidado

        self.green.desligar()
        self.yellow.ligar()
        
        # self.red.desligar()
        

    def nome(self):
        return self.nome
        

    def sensores(self, *args):
        # sensores ficam lendo infinitamente
       while True:
          s1 = not GP.input(self.s1)
          s2 = not GP.input(self.s2)
        
          if s1: 
             if semaforos[not self.nome].estado == fechado:
                self.abrirCuidado()
             else: 
                fecha = thread(None, self.fechar, None, (base, 0))
                fecha.start()
                
             sleep(1)
            
             
class Cor:
    def __init__(self, led, estado, nome):
        self.led = led
        self.estado = estado
        self.nome = nome
        GP.setup(led, GP.OUT)

    def desligar(self):
        GP.output(self.led, False)

    def ligar(self):
        GP.output(self.led, True)

    def inicio(self):
        if self.nome == 'green':
            self.estado = True
        else:
            self.estado = False
        GP.output(self.led, self.estado)
