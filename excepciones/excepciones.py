def sumar_dos():
    while True:
        a=input("Numero 1: ")
        b=input("Numero 2: ")
        # Si el try lanza exception
        # se ejecuta except
        # sino el else
        try:
            resultado = int(a) + int(b)
            # la excepcion a veces lleva el nombre especifico
        except ValueError as e:
            print("Te pedi un numero, salame, no te regales")
            # muestra el nombre del error
            print(f"ERROR: {type(e).__name__}")
        else:
            break
        # el finally se ejecuta al final pase lo que pase
        finally:
            print("Manejo de excepcion finalizado")
    return resultado

print(sumar_dos())