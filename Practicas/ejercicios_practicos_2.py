#falto el profe y los chicos hacen la clase
#A) Pedir el nombre y la edad de los compañeros y ordenar de mayor a menor
#B) El mayor de la clase es el profesor y el menor el asistente
#pedir el nombre y la edad de los compañeros
def obtener_compañeros(cantidad):
    compañeros =[]
    for _ in range(7):
        nombre = input("ingree el nombre del compañero: ")
        edad =int(input("ingrese la edad del compañero: "))
        compañero = (nombre,edad)
        compañeros.append(compañero)
    compañeros.short(key=lambda x:x[1])
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    return asistente, profesor

asistente, profesor = obtener_compañeros(5)
print(f"el profesor es {profesor} y el asistente es {asistente}")

#Este codigo muestra el primer elemento(profesor) de la lista
# y el ultimo (asistete)