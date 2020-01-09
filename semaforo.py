from threading import Thread as thread
from Semaforo_Model import Semaforo
import RPi.GPIO as GP

# semaforo1 = None
# semaforo2 = None

GP.setmode(GP.BCM)
GP.setwarnings(False)

# define os dois sensores de um semaforo
semaforo1 = Semaforo(s1=18, s2=8, nome=0)

# define os pinos dos leds usados
semaforo1.Leds(red=4, yellow=3, green=2)

# define os sensores de um semaforo
semaforo2 = Semaforo(s1=12, s2=10, nome=1)

# define os pinos dos 3 leds usados
semaforo2.Leds(red=21, yellow=20, green=16)

# deixa o semaforo no estado inicial, apenas com o verde ligado


def iniciar():
    semaforo1.inicio()
    semaforo2.inicio() 


def inp(*args):
    while True: 
        a = input()
        iniciar()
        
# ----------------------INICIO DO CODIGO--------------------------------#

iniciar()
thread(None,inp,None,(0,0)).start()








