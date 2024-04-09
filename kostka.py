#!/usr/bin/env python3
#horalka
import random 

class Kostka:

    def __init__(self, steny = 6):
        self.pocet_sten = steny

    def __str__(self):
            return f'Kostka s {self.__pocet_sten} stenami.'


    def hod(self):
       return random.randint(1,self.__pocet_sten)

    def getPocetSten(self):
        return self.__pocet_sten 

K1 = Kostka()
print(K1)
print(k1.getPocetSten()+10)
print(K1.hod())
K2 = Kostka()
print(K2)