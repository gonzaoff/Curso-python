class Gato():
    def sonido(self):
        return "miau"

class Perro():
    def sonido(self):
        return "guau"

# la variable establecida en la función 
# sirve solo para crear algo modificable. 
# Al usar la función “hacer_sonido(animal)”,
# se cambia la variable “animal” por 
# la variable definida como objeto
def hacer_sonido(animal):
    print(animal.sonido())

gato=Gato()
perro=Perro()


# hacer_sonido(perro)

# [------------------------------------------]

def recorrer(elemento):
    for item in elemento:
        print(f"El elemento actual es: {item}")

lis=[1,2,3,4]
lis2=["maquina","como","andas"]

# recorrer(lis2)











