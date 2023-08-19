# Ejercicio de herencia y uso de super:
# Crear un sistema para una escuela. En este sistema, vamos a tener dos clases principales:
# Persona y Estudiante. La clase Persona tendrá los atributos de nombre y edad y un método
# que imprima el nombre y la edad de la persona. La clase Estudiante heredará de la clase
# Persona y también tendrá un atributo adicional: grado y un método que imprima el grado del
# estudiante.
# Deberás utilizar super en el método de inicialización (init) para reutilizar el código de la clase padre
# (Persona). Luego crea una instancia de la clase Estudiante e imprime sus atributos y utiliza sus
# métodos para asegurarte de que todo funciona correctamente

class persona():
    def __init__(self, nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def datos(self):
        print(f"soy {self.nombre}")
        print(f"tengo {self.edad}")
persona1=persona("gonzalo",22)
# persona1.datos()

class estudiante(persona):
    def __init__(self, nombre,edad,grado):
        super().__init__(nombre,edad)
        self.grado = grado
    def datos(self):
        print(f"""Hola, soy {self.nombre} tengo {self.edad}, voy a {self.grado} grado.""")

persona1=estudiante("Leo",20,"8vo")
persona1.datos()



