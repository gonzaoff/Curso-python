# Importamos modulos de carpetas desde local
# La carpeta debe contener un archivo "__init__.py"
# para ser tomado como paquete

# Corroborando que sea un paquete (<class 'list'>)
import paquetes as P1
print(type(P1.__path__))

# Importando modulo con rename (se debe importar el modulo)
import paquetes.sal2 as P2
print(P2.saludar("Gonza"))

# Importando subpack 
import paquetes.subpaquete.sal2 as P3
print(P3.saludar("Sibofit"))

