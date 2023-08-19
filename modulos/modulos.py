# Importar funciones (def) especificas
from modulo_saludar import saludar,saludar2

saludo=saludar("Gonza")
saludo2=saludar2("Sibofit")

print(f"Este es el saludo1: {saludo}")
print(f"Este es el saludo2: {saludo2}")

# Importar funciones y cambiar el nombre de valores especificos
from modulo_saludar import saludar as S,saludar2 as S1

saludo3=S1("Sfit")
saludo4=S("Gon")

print(f"este es el saludo3: {saludo3}")
print(f"este es el saludo4: {saludo4}")

# Importar el modulo y cambiar nombre para facil acceso
import modulo_saludar as m_s

saludo5=m_s.saludar("gonza")

print(f"este es el saludo5: {saludo5}")

# Para ver las propiedades y metodos en el modulo
# print(f"Esto se encuentra dentro del modulo: {dir(m_s)}")

# Acceder a modulos dentro de carpetas(debe estar dentro de la carpeta de posicion)
import Carpeta.mod_en_carpeta as m_ss

saludo6=m_ss.saludar("Locologo")

print(f"este es el saludo5: {saludo6}")