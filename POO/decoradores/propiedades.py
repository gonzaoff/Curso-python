class Persona:
    def __init__(self, nombre,edad,nacionalidad):
        self._nombre = nombre
        # Creo las variables protegidas
        self.__edad = edad
        # Creo la variable privada
        
        self._nacionalidad = nacionalidad
    @property
    # defino como propiedad (x.propiedad)
    def get_nombre(self):
        return self._nombre
    # accedo a la variable protegida
    # mediante una función
    @property
    def get_edad(self):
        return self.__edad
        # acceso a la variable privada solo desde la clase
    @property
    def nacionalidad(self):
        return self._nacionalidad
    @nacionalidad.setter
    # defino un setter de la funcion "nacionalidad"
    def s_nac(self,new_nacionalidad):
        self._nacionalidad = new_nacionalidad
    @nacionalidad.deleter
    # defino un eliminador de la variable nacionalidad
    def nac(self):
        del self._nacionalidad 


gonza=Persona("Gonza",22,"Argentino")



nacionalidad = gonza.nacionalidad
print(nacionalidad)

del gonza.nac

# Setteo la variable otro contenido
nacionalidad = gonza.nacionalidad

print(nacionalidad)




