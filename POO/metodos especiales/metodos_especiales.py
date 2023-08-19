class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def __str__(self):
        return f"Persona(nombre={self.nombre},edad={self.edad})"
    def __repr__(self):
        return f'Persona("{self.nombre}",{self.edad})'
    def __add__(self,otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre+otro.nombre,nuevo_valor)
        

# Objetos
marcos=Persona("Marcos",40)
gonza=Persona("Gonza",22)

# Hace uso del "__str__" Para mostrar el contenido de la clase
print(gonza)

# Hace uso del representante "__repr__"
repre=repr(gonza)
## reconstruyo el objeto usando "eval(representacion)"
### para usarlo desde otra variable
resultado = eval(repre)
#### Objeto modificado
print(resultado.edad)

# La sumatoria de los nombres y las edades
nueva_persona=gonza+marcos
print(nueva_persona)





