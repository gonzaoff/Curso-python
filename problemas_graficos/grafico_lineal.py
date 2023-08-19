import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sms

df = pd.read_csv("problemas_graficos\\pedos.csv")

# Realizar un grafico con sms.lineplot()
sms.lineplot(x="fecha",y="pedos",data=df)

# Determinando un punto en el grafico
plt.plot("01-09",17,"o")

# Mostrar el grafico
plt.show()

























