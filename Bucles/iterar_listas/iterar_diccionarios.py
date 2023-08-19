#diccionario modo js (No puedo crear diccionarios vacios)
diccionario = {
    "Nombre" : "Gonzalo",
    "Apellido" : "Escobar",
    "Edad" : 22
}

#Estructura para mostrar ('<clave>',<valor>')
for key in diccionario.items():
    print(key)

#estructura para solicitar datos por separado
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"la clave es: {key} y el valor es: {value}")
else:
    print("OLA KE ASE")


