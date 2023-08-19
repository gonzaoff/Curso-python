# Principio de responsibilidad unica 
# (Single responsibility principle).
# La nocion de que un objeto solo deberia
# tener una unica razon para cambiar

class TanqueDeCombustible():
    def __init__(self):
        self.combustible = 100
    def agregar_combustible(self,cantidad):
        self.combustible += cantidad
    def obtener_combustible(self):
        return self.combustible
    def usar_combustible(self,cantidad):
        self.combustible -= cantidad

class Auto():
    def __init__(self,tanque):
        self.posicion = 0
        self.tanque = tanque
    def mover(self,distancia):
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2) 
            return "Has movido el auto correctamente."
        else:
            return "No hay combustible."
    def obtener_posicion(self):
        return self.posicion


tanque=TanqueDeCombustible()
autito=Auto(tanque)

print(autito.obtener_posicion())
print(autito.mover(40))
print(autito.obtener_posicion())
print(autito.mover(70))
print(autito.obtener_posicion())
print(autito.mover(40))
print(autito.obtener_posicion())
print(autito.mover(70))
print(autito.obtener_posicion())





