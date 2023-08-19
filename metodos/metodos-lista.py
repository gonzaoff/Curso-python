lista = ["hola", "gonzalo", 22, 44.6, True]

#conteo de elementos
cantidad_elementos = len(lista)

#agregar a la lista "append"
lista.append("Curso python")

#agrega elemento en el indice especifico
#lista.insert(3, ) #(3, <agregar valor>)

#agregar varios elementos a la lista
lista.extend([False, "Mamamia", 2323])

#Eliminar elementos de la lista segun su indice
lista.pop("indice en negativo")

#remueve un elemento segun su valor
lista.remove("valor")

#elimina toda la lista
lista.clear()

print(lista)
