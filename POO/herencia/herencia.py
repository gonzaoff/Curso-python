class ClasePadre:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    def hablar(self):
        return "Hola, soy la clase padre ."

class empleado(ClasePadre):
    def __init__(self,nombre,edad,nacionalidad,trabajo,salario):
        # Forma de heredar "super().__init__(variables,de,clasepadre)"
        super().__init__(nombre,edad,nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
        
    def hablar(self):
        return "NO"

class estudiante(ClasePadre):  
    def __init__(self,nombre,edad,nacionalidad,notas,universidad):
        super().__init__(nombre,edad,nacionalidad)
        self.notas = notas
        self.universidad = universidad

gonzalo=empleado("gonzalo",22,"arg","arq",23323)

trabajador1 = empleado("Robert",23,"Argentina","Arquitecto",230303)

universitario1 = estudiante("Eduardo",40,"argentino",9,"UNRaf")

print(gonzalo.hablar())

# print(universitario1.notas)

# ---------------------------------------------- #

