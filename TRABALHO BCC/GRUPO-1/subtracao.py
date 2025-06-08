def sub_matrizes(matriz1, matriz2):
    linhas = len(matriz1)
    colunas = len(matriz1[0])

    # Verifica se as dimensões são compatíveis
    if linhas != len(matriz2) or colunas != len(matriz2[0]):
        print("Erro: as matrizes devem ter o mesmo tamanho.")
        return None

    # Cria matriz resultado
    subtracao = []
    for i in range(linhas):
        linha_sub = []  # nova linha da matriz soma
        for _ in range(colunas):
            valor = matriz1[i][_] - matriz2[i][_]  # subtração dos elementos
            linha_sub.append(valor)  # adiciona valor subtraido
        subtracao.append(linha_sub)  # adiciona linha à matriz final

    return subtracao

A = [
    [1, 2, 3],
    [4, 5, 6]
]
B = [
    [6, 5, 4],
    [3, 2, 1]
]

print(f"Matriz 1:")
for i in range(len(A)):
    print(A[i])
print(f"\nMatriz 2:")
for i in range(len(B)):
    print(B[i])

# Aplicando a soma
subtracao = sub_matrizes(A, B)

# Exibindo resultado das somas
print("\nSubtração das Matrizes:")
for linha in subtracao:
    print(linha)