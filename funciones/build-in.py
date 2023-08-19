numeros = [4,6,2,88,34,242,34,25,9]


# Encontrando el numero mayor en una lista
numero_mas_alto = max(numeros)
print(numero_mas_alto)
print()

# Encontrando el numero mayor en una lista
numero_menor = min(numeros)
print(numero_menor)
print()

# Redondeando a 6 decimales "round(<numero>,<cantidad_de_decimales>)"
redond=round(12.345,2)
print(redond)
print()

#retorna false -> 0, vacio, falso, none
#retorna True -> distinto de 0, cadena, dato
resultado_bool = bool(None)
resultado_true = bool(1)
print(resultado_bool)
print(resultado_true)
print()

#retorna True, si todos los valores son verdaderos
#en listas o elementos iterables
resultado_all = all([0,True,[166,342]])
resultado_all2 = all([[],True,[123,"algo"]])
print(resultado_all, resultado_all2)
print()

#suma todos los valores del iterable
suma_total = sum(numeros)
print(suma_total)

