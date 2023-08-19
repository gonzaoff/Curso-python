#dicccionario = {
#    "Nombre" : "Gonzalo",
#    <Clave> : <Valor>,
#}


dicccionario = {
    "Nombre" : "Gonzalo",
    "Apellido" : "Escobar",
    "Edad" : 22
}

#Devuelve las claves
clave = dicccionario.keys()

#Devuelve el valor de una clave (si no lo encuentra el programa continua)
valor_de_clave = dicccionario.get()

#Elimina todos los elementos
clear = dicccionario.clear()

#Elimina una clave
del_1_elemento = dicccionario.pop()

#Para iterar el diccionario
dicccionario.items()