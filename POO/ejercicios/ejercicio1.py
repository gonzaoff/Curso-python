class estudiante:
    def __init__(self,nombre,edad,grado): #propiedades
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def estudiar(self):
        print(f"El estudiante {self.nombre} está estudiando")

estudiante1 = estudiante(input("Nombre del Estudiante: "),input("Edad del estudiante: "),input("Grado del estudiante:"))
estudiante2 = estudiante(input("Nombre del Estudiante: "),input("Edad del estudiante: "),input("Grado del estudiante:"))
estudiante3 = estudiante(input("Nombre del Estudiante: "),input("Edad del estudiante: "),input("Grado del estudiante:"))

estudiante1.estudiar()
estudiante2.estudiar()
estudiante3.estudiar()