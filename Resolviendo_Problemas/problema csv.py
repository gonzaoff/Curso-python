#cambiar el formato de la lista
import pandas as pd

df = pd.read_csv("Resolviendo_Problemas\\Archivo_csv.csv")

# Convertir los datos de una columna
df["edad"] = df["edad"].astype(str)

# Muestro el tipo de dato del primer dato
# de la columna "edad"
print(type(df["edad"][0]))

# Reemplaza todos los string que tengan el mismo valor
# df[<"columna">].replace("<reemplazar>",<"reemplazo">,inplace=True)
df["apellido"].replace("Escobar","Maestro",inplace=True)
print(df["apellido"])

# Eliminar datos faltantes
df = df.dropna()
# Elimina las columnas con datos faltantes
df = df.dropna(axis=1)

# Elimina las filas repetidas
df= df.drop_duplicates()


# Creando un csv con el dataframe resultante
df.to_csv("Resolviendo_Problemas\\Archivo_limpio.csv")





