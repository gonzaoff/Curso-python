# Principio de segregascion de la interfaz
# (Interface segregation principle)
# La nocion de que "muchjas interfaces 
# cliente especificas son mejores que 
# una interfaz de proposito general"

from abc import ABC, abstractclassmethod

class Trabajador(ABC):
    @abstractclassmethod
    def trabajar(self):
        pass

class Durmiente(ABC):
    @abstractclassmethod
    def dormir(self):
        pass

class Comedor(ABC):
    @abstractclassmethod
    def comer(self):
        pass

class Humano(Trabajador,Durmiente,Comedor):
    def comer(self):
        print("el humano esta comiendo")
    def trabajar(self):
        print("el humano esta trabajando")
    def dormir(self):
        print("El humano duerme")

class Robot(Trabajador):
    def trabajar(self):
        print("el robot esta trabajando")

gonza=Humano()
gonza.comer()

XLR8=Robot()
XLR8.trabajar()


