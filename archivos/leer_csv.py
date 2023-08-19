import csv

with open("archivos\\Archivo_csv.csv") as archivo:
    reader= csv.reader(archivo)
    for row in reader:
        print(row)