#creando una funcion simple
def saludo1():
    print("Hola maestro, todo bien?")

#ejecutando la funcion
# saludo1()

#Creando funcion con parametros
def saludo2(nombre):
    print(f"Hola {nombre} Como andas?")
#ejecutando la funcion
# saludo2(input())

#Creando funcion por genero.
def saludo3(nombre,genero):
    print("Que pue lo que so vo?")
    print(f"Como te llama?{input(nombre)}")
    genero=genero.lower()
    if (genero == "mujer"):
        adjetivo = "reina"
    elif genero == "hombre":
        adjetivo = "rey"
    else: {
        "vo... coso"
    }

    print(f"Hola {nombre}, Como te va {adjetivo}?")

#Ejecuta el codigo
# saludo3(input(),input())

#Crea una funcion que nos retorna valores
def crear_contraseña_aleatoria(num):
    chars = "abcdefghij"
    numero_entero=str(num)
    num=int(numero_entero[0])
    c1 = num -2
    c2 = num
    c3 = num -5
    return f"{chars[c1]}{chars[c2]}{chars[c3]}{num * 2}",num

password,primer_numero = crear_contraseña_aleatoria(input())
print(f"tu nueva contraseña es {password}")
print(f"Con el numero {primer_numero}")