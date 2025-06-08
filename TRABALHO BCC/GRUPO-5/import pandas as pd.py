import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx
import matplotlib.pyplot as plt


dados = pd.DataFrame.from_dict({   #cria o dataframe com a biblioteca do panda, e com o dataset
    "Luis Gustavo Dias Frigeri": ['phonk', 'rock', 'heavy metal'],
    "Marcos Vinicius": ['sabaton', 'iron maiden', 'insomnium'],
    "Luiz Otavio Vieira Martins Guimaraes": ['charlie brown jr', 'jota quest', 'rosa de saron'],
    "Lucas Pereira": ['link do zap', 'gp da zl', 'joji'],
    "Vitor": ['menos e mais', 'israel e rodolfo', 'kendrick lamar'],
    "Joao Celso da Silva Nogueira dos Santos": ['linkin park', 'pink floyd', 'megadeath'],
    "Vinicius Oliveira": ['bringmethehorizon', 'novulent', 'signcrushesmotorist'],
    "Jonathan": ['bee gees', 'backstreet boys', 'west life'],
    "Portaluppi": ['marino', 'the neighbourhood', 'twenty one pilots'],
    "Rafael": ['linkin park', 'system of a down', 'bruno e marrone'],
    "Luiz Felipe": ['nirvana', 'gorillaz', 'ac/dc'],
    "Karol": ['slipknot', 'raimundos', 'charlie brown jr.'],
    "Nicolas Augusto Cardoso": ['projeto sola', '5 a seco', 'attos 2'],
    "Luiz Antonio Marcussi Neto": ['guns n roses', 'legiao urbana', 'beatles'],
    "Kaio Enrique": ['system of down', 'slipknot', 'linkin park'],
    "Kendy H.": ['iron maiden', 'linkin park', 'imagine dragons']
}, orient='index') # faz com que os nomes sejam as linhas e as bandas sejam as colunas

#transforma as listas de bandas em textos unicos
textos = [' '.join(bandas) for bandas in dados.values]  

#essa biblioteca transforma os textos em vetores numericos comparaveis
vectorizer = TfidfVectorizer()
matriz = vectorizer.fit_transform(textos)


sim = cosine_similarity(matriz)  #calcula a similaridade

#constroi o grafo de similaridade
nomes = dados.index
G = nx.Graph()

for i, nome_i in enumerate(nomes): 
    for j, nome_j in enumerate(nomes):  #esses dois FOR vao passar por todas as listas e comparar todos os pares possiveis
        if i < j and sim[i, j] > 0.1:  #compara e funciona se o grau de similaridade for maior q 0.1
            G.add_edge(nome_i, nome_j, weight=round(sim[i, j], 2))

#exibição do grafo
plt.figure(figsize=(10, 6))
nx.draw(
    G, 
    with_labels=True, 
    node_color='lightgreen', 
    edge_color='gray', 
    font_size=8
)
plt.title("Grafo de Similaridade entre Gostos Musicais")
plt.show()
