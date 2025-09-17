import requests
from bs4 import BeatifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# URLs do site Wordometers
url_world = "https://www.worldometers.info/world-population/"
url_brazil = "https://www.worldometers.info/world-population/brazil-population/"

# Fazer requisição HTTP e pegar o HTML da página
resp = requests.get(url_world)
print("Status da requisição:", resp.status_code) # 200 = OK

# Usar BeautifulSoup para analisar o HTML
soup = BeautifulSoup(resp.text, "html.parser")

# Visualizar os primeiros 500 caracteres do HTML
print(soup.prettify()[:500])
soup

# Buscar a tabela pelo id "example2"
table = soup.find("table", attrs={"id": "example2"})

# Conferir se a tabela foi encontrada
print("Tabela encontrada:", table is not None)
table

# Converter a tabela para Dataframe usando pandas
df_world = pd.read_html(str(table))[0]

# Mostrar as primeiras linhas
df_world.head()

plt.figure(figsize=(10,6))
sns.lineplot(data=df_world, x="Year", y="Population")
plt.title("Projeção da População Mundial até 2050")
plt.ylabel("População (em bilhões)")
plt.xlabel("Ano")
plt.show()