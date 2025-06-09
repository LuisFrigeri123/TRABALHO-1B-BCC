from networkx import Graph

"""
identificar vértices - OK
contagem do número de vértices - OK
identificar ligações - OK
contagem do número de arestas - OK
graus do vértices - OK
grau médio - OK
pesos do grafo - OK
força de conectividade média - OK
densidade - OK
"""

def calcular(G: 'Graph') -> None:
    # vértices e os graus
    print("\nVértices (nós) e seus graus:")
    for vertice, grau in G.degree():
        print(f"{vertice}: {grau}")
        
    # arestas e os pesos
    print("\nArestas (ligações) e seus pesos:")
    for origem, destino, data in G.edges(data=True):
        print(f"{origem} -> {destino}: {data['weight'] if data else "Sem peso"}") # acessa o peso, esse 'data' é um dict

    print("\nPrincipais métricas:\n")

    # total de vértices e arestas
    print(f"Total de vértices: {G.number_of_nodes()}")
    print(f"Total de arestas: {G.number_of_edges()}")

    # grau de conectividade média
    # média aritmética dos graus de conectividade do grafo
    soma_dos_graus = 0
    quantidade_de_graus = 0
    for _, grau in G.degree(): # só precisamos do grau que o G.degree() retorna
        soma_dos_graus += grau
        quantidade_de_graus += 1
        
    grau_medio = soma_dos_graus / quantidade_de_graus
    print(f"Grau de conectividade média: {grau_medio:.2f} ({grau_medio})")

    # força de conectividade média
    # média aritmética dos pesos das arestas
    if list(G.edges(data=True))[0][2]:
        soma_dos_pesos = 0
        quantidade_de_pesos = 0
        for _, _, data in G.edges(data=True): # só precisamos dos pesos que essa função retorna
            soma_dos_pesos += data['weight']
            quantidade_de_pesos += 1
        
        peso_medio = soma_dos_pesos / quantidade_de_pesos
        print(f"Força de conectividade média: {peso_medio:.2f} ({peso_medio})")
    else:
        print(f"Força de conectividade média: O Grafo não tem peso")

    # densidade 
    # razão entre a qnt de ligações existentes no grafo e relações possíveis
    vertices = G.number_of_nodes()
    ligacoes = G.number_of_edges()
    densidade = (2 * ligacoes) / (vertices * (vertices - 1)) 
    print(f"Densidade: {densidade} ou {densidade*100:.0f}% conectada.")
    