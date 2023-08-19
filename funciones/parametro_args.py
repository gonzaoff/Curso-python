#forma no optima de sumar valores
def suma(lista):
    numeros_sumados=0
    for numero in lista:
        numeros_sumados = numeros_sumados + numero
    return numeros_sumados

resultado = suma([5,4,22,7,34,99])

# Forma optima de sumar valores
def suma_total(numeros):
    return sum([*numeros])

resultado2 = suma_total([5,22,342,1])
print(resultado2)

#otra forma de sumar valores
def suma(nombre, *numeros):
    return f"{nombre} la suma de los numeros es {sum(numeros)}"

resultado = suma(input(),5,4,22,7,34,99)
print(resultado)

