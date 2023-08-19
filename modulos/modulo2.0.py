# Importo el modulo desde la carpeta
import Carpeta.mod_en_carpeta
print(Carpeta.mod_en_carpeta.saludar("Gonza"))

# Importo el modulo y lo renombro
import Carpeta.mod_en_carpeta as m_s
print(m_s.saludar("Sibofit"))

# Importo desde otra carpeta
import sys
# Comando para agregar ruta
sys.path.append("c:\\Users\\Gonza\\Desktop\\UNRAF (Actualizado 13-04)\\Pensamiento Computacional\\Resuelto\\Curso python")
print(sys.path)

import mod_fuera as m_f

saludo=m_f.saludar("Gonza")
print(f"este es el saludo 1: {saludo}")

