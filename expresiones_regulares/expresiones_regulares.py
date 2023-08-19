import re

texto = """hola maestro, esta es la cadena 1. como estas?
estas es la 425daddddd linea de codigo
y esta es la 324ra linea definitiva el capitan"""

# Buscando palabras
resultado = re.search("estas", texto)
# Buscando una palabra especifica
resultado1 = re.findall("estas", texto)
# Buscando una palabra en mayus y en minus
resultado2 = re.findall("estas", texto, flags=re.IGNORECASE)
# print(resultado2)

# "\d" busca digitos numericos del 0-9
resultado3=re.findall(r"\d",texto)

# "\D" busca todo menos digitos numericos
resultado4=re.findall(r"\D",texto)

# "\w" busca caracteres alfanumericos (a-z, A-Z, 0-9, _)
resultado5=re.findall(r"\w",texto)

# "\W" busca todo menos caracteres alfanumericos (a-z, A-Z, 0-9, _)
resultado6=re.findall(r"\W",texto)

# "\s" busca espacios en blanco
resultado7=re.findall(r"\s",texto)

# "." busca todo menos saltos en linea
resultado8=re.findall(r'.',texto)

# "\n" busca los saltos en linea
resultado9=re.findall(r"\n",texto)

# "\." Cancela todos los caracteres especiales, cancelando la funcion del punto
# y buscando puntos
resultado9=re.findall(r'\.',texto)

# armando una cadena que busque un numero seguido de un punto
# y un espacio normal (abc) no (a,b,c)
resultado10=re.findall(r"\d\.\s",texto)

# "^" Busca el principio de una linea
resultado11=re.findall(r"^hola",texto)
# "^" buscando multilinea (post "\n")
resultado111=re.findall(r"^hola",texto,flags=re.M)

# "$" busca al final de cada linea
resultado12=re.findall(r"capitan$",texto, flags=re.M)

# {n} busca "n" cantidad de digitos
res1=re.findall(r"\d{3}",texto)

# {n,m} busca por lo menos "n" cantidad de digitos y 
# como maximo "m" cantidad de digitos
res2=re.findall(r"\d{3,5}",texto)

# {n,m} busca por lo menos "n" cantidad de veces repetido 
# el ultimo caracter y como maximo "m" cantidad de veces
# repetidos el ultimo caracter
res3=re.findall(r"ad{3,5}",texto)

# (ab){n,m} busca al grupo (ab) por lo menos 
# "n" cantidad de veces y como maximo "m" cantidad 
# de veces repetidos el grupo
res3=re.findall(r"(ad){3,5}",texto)

# | -> busca una cosa o la otra
res4=re.findall(r"\d{2,4}|hola",texto)
# Busca numeros de 2 a 4 cifras O la cadena "hola"

# busca y reemplaza re.sub()
res5=re.sub(r"^hola", "Halo",texto)

# busca y reemplaza sin importar el orden re.sub("[ABC]")
res6=re.sub("[a]", "*", texto)
print(res6)




#


