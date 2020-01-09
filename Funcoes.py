import _thread as thread, time
import RPi.GPIO as GP
from Semaforo_Model import Semaforo

passaCarro = 5

red1 = Semaforo(1)
yellow1 = Semaforo(1)
green1 = Semaforo(1)

red2 = Semaforo(1)
yellow2 = Semaforo(1)
green2 = Semaforo(1)

a1 = 7
b1 = 8

a2 = 9
b2 = 10

s1 = 11
s2 = 12

GP.output()
GP.input()

def Inicio():
    GP.output(Semaforo1[green1], True)
    GP.output(Semaforo2[green2], True)
    GP.output(Semaforo1[yellow1], False)
    GP.output(Semaforo2[yellow2], False)
    GP.output(red1, False)
    GP.output(red2, False)


def Apagar_All(s):
    if s == 1:
        GP.output(green1, False)
        GP.output(yellow1, False)
        GP.output(red1, False)
    else:
        GP.output(green2, False)
        GP.output(yellow2, False)
        GP.output(red2, False)


# ---------------------------- VERDE - VERMELHO ---------------------------#

def Verde_Vermelho(s, r):
    if not s:
        Apagar_All(s)
        GP.output(r, True)


def Verde_Vermelho_1():
    Verde_Vermelho(s1, red1)


def Verde_Vermelho_2():
    Verde_Vermelho(s2, red2)


# ---------------------------- AMARELO - VERMELHO ---------------------------#

def Amarelo_Vermelho():
    pass
