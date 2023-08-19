class Persona:
    def __init__(self, nombre,edad,nacionalidad):
        self._nombre = nombre
        # Creo las variables protegidas
        self.__edad = edad
        # Creo la variable privada
        
        self._nacionalidad = nacionalidad
    def get_nombre(self):
        return self._nombre
    # accedo a la variable protegida
    # mediante una función
    def get_edad(self):
        return self.__edad
        # acceso a la variable privada solo desde la clase
    def get_nacionalidad(self):
        return self._nacionalidad
    def set_nacionalidad(self,new_nacionalidad):
        self._nacionalidad = new_nacionalidad

gonza = Persona("Gonza", 22, "argentino")






