
#el tipo Lista[] es modificable.
lista = ["sintesis", True, 1.85]
lista[2] = 1.90 #valido
print(lista) #"true" es el elemento 2 en indice 1.

#las Tuplas() no son modificables
tupla = ("sintesis", True, 1.85)
tupla[2] = 1.83 #invalido
print(tupla)

#conjunto (set)
conjunto = {"sintesis", True, 1.85}
    #se puede redefinir completo, no sustituir elementos.
    #no almacena datos duplicados

#diccionario
    #clave : valor, [key : value,]
diccionario = {
    "nombre" : "gonzalo Escobar",
    "edad" : 22,
    "altura" : 1.80,
    "Le gusta programar?" : True,
    
}

print(diccionario["nombre"])





