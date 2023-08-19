import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("problemas_graficos\\cofla_ingresos.csv")
# Mostrando las columnas existentes
print(df.columns)

#Creando grafico
sns.barplot(data=df, x="fuente", y="Ingresos")
total_ingresos=df["Ingresos"].sum()
print(f"el total de los ingresos es de ${total_ingresos}")
#Mostrando grafico
plt.show()























