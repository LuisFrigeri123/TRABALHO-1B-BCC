def transpor_matriz(matriz):
    linhas = len(matriz)      # número de linhas da matriz original
    colunas = len(matriz[0])  # número de colunas da matriz original

    transposta = []
    for _ in range(colunas):
        nova_linha = []  # nova pra matriz transposta linha da matriz transposta
        for i in range(linhas):
            nova_linha.append(matriz[i][_])  # adiciona o elemento da posição invertida
        transposta.append(nova_linha)  # adiciona a linha na transposta

    return transposta

A = [
    [1, 2, 3],
    [4, 5, 6]
]
print(f"Matriz original:")
for i in range(len(A)):
    print(A[i])

# Aplicando a função
transposta = transpor_matriz(A)

# Exibindo o resultado
print("\nMatriz Transposta:")
for linha in transposta:
    print(linha)