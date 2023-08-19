#Creando mi exception
class MiExcepcion(Exception):
    def __init__(self,err):
        print(f"impresionante, cometiste el siguiente error: {err}")

# Lanzando exception
# raise MiExcepcion("sin manejar exception")

# Manejandola
try:
    raise MiExcepcion("jaja enfermito")
except Exception:
    print("Como vas a comenter ese error")