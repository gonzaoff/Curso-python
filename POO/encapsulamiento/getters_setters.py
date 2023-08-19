import encapsulamiento as en
#Objeto/s:
gonza = en.Persona("Gonza", 22, "argentino")

# --- Getters ---
nombre = en.gonza.get_nombre()
edad = en.gonza.get_edad()
print(nombre,edad)

# print(gonza.__edad) 
# devuelve que no existe la variable ".__edad"

# --- Setters ---
nacionalidad = en.gonza.get_nacionalidad()
# acceso a la variable "nacionalidad" 
## mostrar el contenido de "._nacionalidad"
print(nacionalidad)


en.gonza.set_nacionalidad("español")
# Setteo la variable otro contenido
nacionalidad = en.gonza.get_nacionalidad()

print(nacionalidad)


# -----------------------

print(gonza)