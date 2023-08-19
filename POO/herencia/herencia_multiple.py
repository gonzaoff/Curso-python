import herencia as hr

class artista:
    def __init__(self, habilidad): 
        self.habilidad = habilidad
    def mostrar_habilidad(self):
        return "mi habilidad es: {self.habilidad}"
    def hablar(self):
        return "soy artista"


class EmpleadoArtista(hr.ClasePadre,artista):
    def __init__(self,nombre,edad,nacionalidad,habilidad,salario,empresa):
        hr.ClasePadre.__init__(self,nombre,edad,nacionalidad)
        artista.__init__(self,habilidad)
        self.salario = salario
        self.empresa = empresa
    def presentarse(self):
        return f"hola, soy: {self.nombre}, {self.mostrar_habilidad()} y trabajo en {self.empresa}"



personaje1=EmpleadoArtista("Raul",23,"argentino","Tocar la guitarra",34000,"alguna empresa")

# consultor de herencia "issubclass(subClase,clasePadre)"
herencia=issubclass(EmpleadoArtista,artista)

# consulto si es un objeto/instancia de una clase "isintance(objeto,clase)"
instancia=isinstance(personaje1,EmpleadoArtista)
#Si hereda de una subclase, hereda tambien de las clases padre.
#Si hereda de clases padre, no hereda de subclases.
print(personaje1.presentarse())
