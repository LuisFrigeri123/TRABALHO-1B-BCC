# Kendy
A = [
    [1, 2, 3], 
    [4, 5, 6]
]
#matrizes de exemplo só pra testar
B = [
    [7, 8, 9],
    [10, 11, 12]
]

print(f"Matriz 1:")
for i in range(len(A)):
    print(A[i])
print(f"\nMatriz 2:")
for i in range(len(B)):
    print(B[i])

resultado = []

for i in range(len(A)):  #len(A) é o número de linhas da matriz A, i vai ser 0 e 1 (ou o número de linhas que a matriz tiver)
    linha = []
    for j in range(len(A[0])): #len(A[0]) é o número de colunas, j vai de 0 a 2 nesse exemplo 
        linha.append(A[i][j] + B[i][j]) #A[i][j] + B[i][j] soma o elemento da linha i e coluna j de A e B
    resultado.append(linha) #adiciona o resultado em uma nova matriz

print("\nResultado da soma:")
for linha in resultado:
    print(linha) #mostra o resultado