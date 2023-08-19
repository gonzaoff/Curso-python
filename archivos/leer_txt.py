# Metodos de lectura y escritura <with open(<"archivos\\texto_de_gonza.txt">,<"w">,encoding="UTF-8") as <Nuevo_Nombre>:
# r – Lectura únicamente.
# w – Escritura únicamente, reemplazando el contenido actual del archivo o bien creándolo si es inexistente.
# a – Escritura únicamente, manteniendo el contenido actual y añadiendo los datos al final del archivo.
# w+, r+ o a+ – Lectura y escritura.


# Abrir archivo de texto
with open("archivos\\texto_de_gonza.txt",encoding="UTF-8") as archivo_a_leer:
    # Leer archivo
    archivo = archivo_a_leer.read()
    print(f"Este print lee el archivo que dice lo siguiente: \n{archivo}\n")

with open("archivos\\texto_de_gonza.txt",encoding="UTF-8") as archivo_a_leer:
    # Leer la primera linea <readlines()>
    lineas = archivo_a_leer.readlines(3)
    print(f"Este print lee la primera sentencia, que dice lo siguiente: \n{lineas}\n")

with open("archivos\\texto_de_gonza.txt",encoding="UTF-8") as archivo_a_leer:
    # Leer caracter por caracter <readline(cantidad de caracteres)>
    linea_xl = archivo_a_leer.readline(10)
    print(f"Este print lee caracter por caracter, que dice lo siguiente: \n{linea_xl}\n")

with open("archivos\\texto_de_gonza.txt","w",encoding="UTF-8") as archivo_a_leer:
    # Agregando (5) lineas 
    for i in range(5):
        sum_linea=archivo_a_leer.write(f"linea {i+1} agregada")
        archivo_a_leer.write("\n")

# with open("archivos\\texto_de_gonza.txt","w",encoding="UTF-8") as archivo_a_leer:
    # sobreescribiendo el archivo
    # sobrescribir = archivo_a_leer.write("""Buenas noches, se comunico con el servicio de informatico Sibolich S.A
# ¿Desea realizar una consulta?""")
    # print(sobrescribir)
    
    ##Escribir en lineas
    # escribir = archivo_a_leer.writelines([" - Hola facha ¿como andas? \n"," - Todo bien, ¿vos? \n"])
    # escribir2 = archivo_a_leer.writelines([" - Bien bien tambien \n", " - Me alegro por vos"])

# Cerrar el archivo
# luego de cerrar el archivo hay que volver a abrirlo
archivo_a_leer.close()