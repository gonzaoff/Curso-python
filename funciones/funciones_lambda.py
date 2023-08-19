numeros = [1,2,3,4,5,6,7,8,9]

#creando funcion para multiplicar por 2 con lambda
multiplicar_por_dos = lambda x : x*2

#creando funcion que diga si es par
def es_par(num):
    if (num%2==0):
        return True

#creando funcion que diga si es impar
def es_impar(num):
    if (num%2==1):
        return True

#usando filter mostrando pares
numeros_pares = filter(es_par, numeros)
print(f"esto es solo filter: {list(numeros_pares)}")
#usando filter mostrando impares
numeros_impares = filter(es_impar, numeros)
print(f"Esto es solo filter: {list(numeros_impares)}")
#usando filter + lambda
numeros_pares = filter(lambda numero:numero%2 == 0, numeros)
print(f"Esto es filter con lambda: {list(numeros_pares)}")
#usando filter mostrando impares
numeros_impares = filter(lambda numero:numero%2 == 1, numeros)
print(f"Esto es filter con lambda: {list(numeros_impares)}")

