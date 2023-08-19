cadena1 = "Hola soy Gonzalo"
cadena2 = "¿Como estas?"

#modo de uso "dato.metodo()"

#convierte los datos en mayusculas
resultado = cadena1.upper()


#convierte los datos en minusculas
resultado1 = cadena1.lower()


#retoma la posicion de la primera similitud en el string(Si, el substring no es encontrado retorna -1.)
resultado2 = cadena1.find("hola")


#retoma la posicion de la ultima similitud en el string(Si, el substring no es encontrado retorna -1.)
resultado3 = cadena1.rfind("Hola")


#Inserta un  ", "  después de cada carácter en un string
resultado4 = ", ".join(cadena1)
##concatena listas de caracteres.
program = ["g","o","n","z","a"] 
#print("".join(program))


#Reemplaza una cadena con otra
resultado5 = cadena1.replace("Hola soy Gonzalo", "Hola soy Gonza") #,numeroDeVeces)


#Mostrar resultados
print(resultado5)