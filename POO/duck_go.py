class Bus:
    def __init__(self):
        self.pasajeros = []
# crea la clase "Bus()" en la que define a-
# self.pasajeros como una lista "[]" .
    def add_pasajero(self,pasajero):
        self.pasajeros.append(pasajero)
# define la funcion "self.pasajeros.append(pasajero)"-
# para agregar valores a la lista denominados "pasajeros".
    def __getitem__(self,asiento):
        return self.pasajeros[asiento]
# define la funcion "__getitem__" para retornar -
# la ubicacion en la lista con el indice "[x]".

bus = Bus();

bus.add_pasajero("Duck Duck Go")
# añade 1 pasajero a la lista
bus.add_pasajero("Duck Duck Go")
bus.add_pasajero("Duck Duck Go")

print(bus[1])

# crea la clase "Bus()" en la que define a-
# self.pasajeros como una lista "[]" .



