import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("problemas_graficos\\bigotes.csv")

# Realizar un grafico con sms.lineplot()
sns.boxplot(x="categoria",y="valor",data=df)

# Mostrar el grafico
plt.show()