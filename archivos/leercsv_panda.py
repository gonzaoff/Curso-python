import pandas as pd

# Usando la funcion read_csv para leer el archivo CSV
df = pd.read_csv("archivos\\Archivo_csv.csv")
df2 = pd.read_csv("archivos\\Archivo_csv.csv")
# print(df)


# Obteniendo los datos de una columna especifica
nombres = df["nombre"]
# print(nombres)


# Redefiniendo columnas
# df = pd.read_csv("archivos\\Archivo_csv.csv",names=["name","lastname","age"])
# print(df)


# Ingreso a valores desde slacy
cadena = "0123456789"
# print(cadena[1:4])


# ordenando el dataframe por edad
df_ascendente=df.sort_values("edad")
# print(df_ascendente)


# Ordenando por edad de forma descendente
df_descendente=df.sort_values("edad",ascending=False)
# print(df_descendente)


# Concatenando dos dataframes
df_concatenado= pd.concat([df,df2])
# print(df_concatenado)


# Accediendo con head() 
# A una cantidad determinada de filas
filas_desde_arriba = df.head(3)
# print(filas_desde_arriba)


# Accediendo a las filas de abajo hacia arriba
# df.tail()
filas_desde_abajo=df.tail(3)
# print(filas_desde_abajo)


# Accediendo a la cantidad total de filas y columnas
# con shape()

## Forma estandar
filas_y_columnas_totales=df.shape
filas_totales = filas_y_columnas_totales[0]
columnas_totales = filas_y_columnas_totales[1]
# print(filas_y_columnas_totales)

##Desempaquetando
filas,columnas=df.shape
# print(filas,columnas)


# Mostrando estadisticas del dataframe
df_info=df.describe()
# print(df_info)


# Accediendo a un elemento especifico con lock[ubicacion,nombre_de_columna]
elemento_especifico = df.loc[2,"edad"]
# print(elemento_especifico)

# Accediendo con ilock[indice,columna]
elemento_por_indice=df.iloc[2,2]
# print(elemento_por_indice)

# accediendo a todas las filas de una columna
apellidos = df.iloc[:,1]
# print(apellidos)

# accediendo a todas las columnas de una fila
datos = df.iloc[2,:]
# print(datos)

# Accediendo a filas "mayor/menor que" df.loc[df["Columna"]>X,:]
mayor_que = df.loc[df["edad"]>50,:]
print(mayor_que)
menor_que = df.loc[df["edad"]<50,:]
print(menor_que)






