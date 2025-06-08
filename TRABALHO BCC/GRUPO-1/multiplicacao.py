matriz = [[1,2],
          [3,4]]
matriz_b = [[2,3,0],
            [3,5,6]]
constante = 4

print(f"Matriz 1:")
for i in range(len(matriz)):
    print(matriz[i])
print(f"\nMatriz 2:")
for i in range(len(matriz_b)):
    print(matriz_b[i])
print(f"\nConstante = {constante}")


def mult_matriz_constante(matriz, constante):
    resultado = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] *= constante
            resultado.append(matriz[i][j])
    if resultado:
      print("\nResultado da multiplicação pr uma constante:")
      for linha in matriz:
        print(linha)
mult_matriz_constante(matriz,constante)
                      
def mult_matriz(matriz, matriz_b):
    resultado = [[0 for i in range(len(matriz_b[0]))] for j in range(len(matriz))]
    if len(matriz[0]) != len(matriz_b):
        print("O número de colunas da Matriz A deve ser igual ao número de linhas da Matriz B")
    else:
        for i in range(len(matriz)): # linha da matriz 1
            for j in range(len(matriz_b[0])): # coluna da matriz 2
                for k in range(len(matriz_b)): # coluna da matriz A pela linha da matriz B
                    resultado[i][j] += matriz[i][k] * matriz_b[k][j]
    if resultado:
        print("\nResultado da multiplicação entre Matrizes:")
        for linha in resultado:
            print(linha)
mult_matriz(matriz,matriz_b)