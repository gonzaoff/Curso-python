#Pido la frase
frase = input("decime un frase y te calculo cuanto tardas en decirla: ")
#Comprendo los espacios que separan a las palabras
palabras_separadas = frase.split(" ")
#Cuento estos espacios
cantidad_palabras = len(palabras_separadas)
#Imprimo los resultados
print(f"dijiste {cantidad_palabras} palabras y tardarias {cantidad_palabras/2} segundos en decirlas.")
print(f"Dalto lo diria en {cantidad_palabras *100 //2 *1.3 /100} segundos")
#If
if cantidad_palabras > 120:
    print("para flaco tampoco te pedi un testamento")




















