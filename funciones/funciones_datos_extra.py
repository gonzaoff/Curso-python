#funcio definida desde el uso de la funcion
def frase (nombre,apellido,adjetivo):
    return f"hola {nombre} {apellido}, como estas {adjetivo}"

frase_resultado = frase("gonzalo", "escobar", "capo")
# print(frase_resultado)

#Funcion definida con forzado de variable
def frase (nombre,apellido,adjetivo):
    return f"hola {nombre} {apellido}, como estas {adjetivo}"

frase_resultado = frase(adjetivo="capo", apellido="Escobar", nombre="Gonzalo")
# print(frase_resultado)

#Funcion con variable definida por el usuario
def frase (nombre,apellido,adjetivo):
    return f"hola {nombre} {apellido}, como estas {adjetivo}"

frase_resultado = frase(adjetivo=input(), apellido=input(), nombre=input())
print(frase_resultado)
