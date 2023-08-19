#creando diccionario con la variable dict() <con posibilidad de crear diccionarios vacios)
diccionario = dict(nombre="gonzalo",apellido="escobar",edad=22)

#diccionario modo js (No puedo crear diccionarios vacios)
dicccionario2 = {
    "Nombre" : "Gonzalo",
    "Apellido" : "Escobar",
    "Edad" : 22
}

#estructura de fromkeys()
#diccionario = dict.fromkeys([<clave1>,<clave2>,<clave...>], <valor asignado a todas las claves>) 

#creando diccionarios con fromkeys() (todas las claves con valor "no se")
diccionario3 = dict.fromkeys(["nombre", "apellido"], "No se")
print(diccionario3)
#creando diccionarios con fromkeys() (todas las claves con valor "none")
diccionario4 = dict.fromkeys(["nombre", "apellido"])
print(diccionario4)

































