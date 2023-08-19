
# "atributos estaticos" todos los objetos que cree
# siempre van a tener estas propiedades
class celular():
    # el atributo es real solo cuando pertenece-
    # a una variable "celular1 = celular()" -> print(celular1.marca)
    Marca = "Samsung"
    modelo = "S23"
    camara = "48MP"

# Objetos
celular1 = celular()
celular2 = celular()
celular3 = celular()
celular4 = celular()

# print(celular1.camara)

class celular:
    def __init__(self,marca,modelo,camara): #propiedades
        self.marca = marca
        self.camara = camara
        self.modelo = modelo
    # Funciones
    def llamar(self):
        print(f"Estas haciendo una llamada desde tu: {self.modelo}")
    def cortar(self):
        print(f"Cortaste la llamada desde tu: {self.modelo}")

# Objetos
celular1 = celular("Samsung","S23","48MP")
celular2 = celular("Apple","iPhone 15 Pro","96MP")
# print(celular2.modelo)

celular2.cortar()






