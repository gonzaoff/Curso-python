import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("problemas_graficos\\dispersion.csv")

# Realizar un grafico con sms.lineplot()
sns.scatterplot(x="tiempo",y="dinero",data=df)

# Mostrar el grafico
plt.show()

























