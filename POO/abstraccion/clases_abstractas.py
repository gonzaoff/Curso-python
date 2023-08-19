from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self, nombre, edad,sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
    
    @abstractclassmethod
    def hacer_actividad(self):
        pass
    
    def presentarse(self):
        print(f"Hola, me llamo: {self.nombre} y tengo {self.edad} años.")

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")

class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
    def hacer_actividad(self):
        print(f"actualmente estoy trabajando en el rubro de: {self.actividad}")


# print("Rellena los campos:")
# persona1=Trabajador(input("Como te llamas?: "),input("Cuantos años tenes?: "),input("Como te autopercibis?: "),input("A que te dedicas?: "))
# persona1.presentarse()
# persona1.hacer_actividad()

gonza = Estudiante("Gonzalo",22,"masculino","programación")
gonza.presentarse()
gonza.hacer_actividad()

# marcos = Trabajador("Marcos",27,"Masculino","Carnicero")
# marcos.presentarse()
# marcos.hacer_actividad()






