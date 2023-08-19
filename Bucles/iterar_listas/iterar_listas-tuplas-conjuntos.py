animales = ["gato","perro","loro","cocodrilo"]
numeros = [52,16,14,72]

#iterando 2 listas del mismo tamaño al mismo tiempo
for numero,animal in zip(animales,numeros):
    print(f"reccoriendo lista 1: {animal}")
    print(f"recorriendo lista 2: {numero}")

#recorriendo la lista animales
for animal in animales:
    print(f"ahora la variable animal es igual a: {animal}")

#recorriendo la lista numeros y multiplicandolos por 10
for numero in numeros:
    resultado = numero * 10
    print(resultado)

#recorriendo una lista desde el 20 a 30-1
for num in range(20,30):
    print(num)

#forma de recorrer una lista con su indice 
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'el indice es: {indice} y el valor es: {valor}')

#forma practica y elegante. 
#estructura:
#for <indice>,<valor en lista> in enumerate(variable_lista)
#else: (se muestra siempre al terminal el for)
#   print("el bucle termino")
for i,num in enumerate(numeros):
    print(i,num)
else:
    print("el bucle termino.")


print("hola que hace")