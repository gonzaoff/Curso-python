def decorador(funcion):   
    def funcion_modificada():
        print("antes de la funcion")
        funcion()
        print("despues de llamar a la funcion")
    return funcion_modificada

# def saludo():
#     print("Hola Gonza")

# def cierre():
#     print("adios saludos")

# saludo_modificado = decorador(saludo,cierre)
# saludo_modificado()

@decorador
def saludo():
    print("Hola Gonza")
saludo()


