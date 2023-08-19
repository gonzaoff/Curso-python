#creando un conjunto con set()
conjunto = set(["dato1","dato2"])

#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato3","dato4"])
conjunto2 = {conjunto1, "dato5"}
#print(conjunto2)

#Teoria de conjuntos
conjunto3 = {1,3,5,7}
conjunto4 = {1,3,7}

#verificando si es un subconjunto
resultado = conjunto4.issubset(conjunto3)
resultado = conjunto4 <= conjunto3
print(resultado)

#verificando si es un superconjunto
resultado2 = conjunto.issuperset(conjunto3)
resultado2 = conjunto3 >= conjunto4
print(resultado2)

#verificando que haya algun resultado en comun (false)
resultado3 = conjunto4.isdisjoint(conjunto3)
print(resultado3)









