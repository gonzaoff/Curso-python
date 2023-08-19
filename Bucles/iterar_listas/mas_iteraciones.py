# sourcery skip: list-comprehension, list-literal
#Creando listas
frutas = ["banana", "manzana", "pera", "naranja", "mandarina", "granada"]
cadena_texto = "Hola mundo como estas?"
numeros = [2,4,76,33,2]

#evitando que coma una ["manzana"]
for fruta in frutas:
    if fruta == "manzana":
        continue
    print(f"me voy a comer una {fruta}")

#termina el codigo despues en el break
for fruta in frutas:
    if fruta == "manzana":
        break
    print(f"me voy a comer una {fruta}")
print("el bucle termino")

#recorriendo/iterando cadenas de texto letra por letra
for letra in cadena_texto:
    print(letra)

#for en una sola linea de codigo:
#estructura basica
numeros_duplicados = list()
for numero in numeros:
    numeros_duplicados.append(numero*2)
print(numeros_duplicados)
#estructura de una sola linea
numeros_duplicados = [numero*2 for numero in numeros]
print(numeros_duplicados)



