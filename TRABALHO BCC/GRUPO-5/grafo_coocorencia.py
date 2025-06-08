import pandas as pd  # importa a biblioteca para manipulação de dados (planilhas, tabelas etc.)
import io  # permite tratar strings como se fossem arquivos
import ast  # permite converter strings que parecem listas em listas reais
import networkx as nx  # biblioteca para criação de grafos/redes
import matplotlib.pyplot as plt  # usada para criar gráficos e visualizações

# dados dos participantes e suas bandas favoritas, em formato de texto
dados = """
Luis Gustavo Dias Frigeri,"['phonk', 'rock', 'heavy metal']"
Marcos Vinicius,"['sabaton', 'iron maiden', 'insomnium']"
Luiz Otávio Vieira Martins Guimarães ,"['charlie brown jr', 'jota quest', 'rosa de saron']"
Lucas Pereira,"['link do zap', 'gp da zl', 'joji']"
Vitor ,"['menos e mais', 'israel e rodolfo', 'kendrick lamar']"
João Celso da Silva Nogueira dos Santos,"['linking park', 'pink floyd', 'megadeath']"
Vinicius Oliveira,"['bringmethehorizon', 'novulent', 'signcrushesmotorist']"
Jonathan ,"['bee gees', 'backstreet boys', 'west life']"
Portaluppi,"['marino', 'the neighbourhood', 'twenty one pilots']"
Rafael,"['linkin park', 'system of a down', 'bruno e marrone']"
Luiz Felipe ,"['nirvana', 'gorillaz', 'ac/dc']"
Karol ,"['slipknot', 'raimundos', 'charlie brown jr.']"
Nicolas Augusto Cardoso,"['projeto sola', '5 a seco', 'attos 2']"
Luiz Antônio Marcussi Neto ,"[""guns n' roses"", 'legiao urbana', 'beatles']"
Kaio Enrique,"['system of down', 'slipknot', 'linkin park']"
Kendy H.,"['iron maiden', 'linkin park', 'imagine dragons']"
"""

# le a string como se fosse um arquivo CSV e cria uma tabela (DataFrame)
df = pd.read_csv(io.StringIO(dados), skiprows=1, header=None, names=["nome", "artistas"])

# converte a coluna de artistas (que está em string) para listas reais
df["artistas"] = df["artistas"].apply(ast.literal_eval)

# cria um grafo (rede) onde os nós são bandas e as ligações são baseadas em gosto em comum
G = nx.Graph()

# para cada lista de bandas de cada pessoa
for lista in df["artistas"]:
    # compara cada banda da lista com as outras bandas da mesma lista
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            a, b = lista[i].strip().lower(), lista[j].strip().lower()  # remove espaços e padroniza para minúsculas
            if G.has_edge(a, b):  # se ja existe conexão entre as bandas
                G[a][b]['weight'] += 1  # aumenta o peso (quantas vezes apareceram juntas)
            else:
                G.add_edge(a, b, weight=1)  # cria a conexão com peso 1 (primeira vez que aparecem juntas)

# configura o tamanho da figura do grafo
plt.figure(figsize=(12, 8))

# define as posições dos nós de forma mais organizada
pos = nx.spring_layout(G, k=0.7)

# desenha o grafo com rótulos (nomes das bandas)
nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='gray', node_size=1000, font_size=9)

# pega os pesos das conexões (quantas vezes bandas aparecem juntas)
labels = nx.get_edge_attributes(G, 'weight')

# desenha os pesos das conexões no grafo
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# define o título do gráfico
plt.title("Grafo de Coocorrência de Bandas Favoritas")

# mostra o grafo
plt.show()