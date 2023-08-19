print("""Bienvenido al buscador de expresiones regulares
Determine la funcion que busca
1) Buscador de palabras
2) Formulas de expresiones regulares""")

i=input("Ingrese la funcion aqui: ")

if i == 1:
    print("""a) Buscar digitos numericos 0-9
b) Buscar caracteres alfanumericos (A-a,0-9,_,)""")
    a = input("ingrese el caracter aqui: ")
    if a=="a":
        print(f""" el buscador de digitos numericos se comporta de la siguiente forma
texto de ejemplo: {texto} 
""")
elif i == 2:
    