import numpy as np

matriz_det = [[1, 2],
              [3, 4]]
print(f"Matriz 1:")
for i in range(len(matriz_det)):
    print(matriz_det[i])

#                    1                 4 
diag_p = matriz_det[0][0] * matriz_det[1][1]
#                    2                 3
diag_s = matriz_det[0][1] * matriz_det[1][0]

calc_det = diag_p - diag_s
print(f"Resultado: {diag_p} - {diag_s} = {calc_det}")



matriz_det2 =[[2, 1, (-3)],
              [3, 2, 4],
              [2, 5, (-2)]]
print("\nMatriz 2:")
for i in range(len(matriz_det2)):
    print(matriz_det2[i])

#calculando diagonais 
#                      2                  1                  -3
diag_p1 = matriz_det2[0][0] * matriz_det2[1][1] * matriz_det2[2][2]
#                      1                  4                  2
diag_p2 = matriz_det2[0][1] * matriz_det2[1][2] * matriz_det2[2][0]
#                     -3                  3                  5
diag_p3 = matriz_det2[0][2] * matriz_det2[1][0] * matriz_det2[2][1]

resultado_diag_p = diag_p1+diag_p2+diag_p3

#                      1                  3                 -2
diag_s1 = matriz_det2[0][1] * matriz_det2[1][0] * matriz_det2[2][2]
#                      2                  4                  2
diag_s2 = matriz_det2[0][0] * matriz_det2[1][2] * matriz_det2[2][1]
#                     -3                  3                  2
diag_s3 = matriz_det2[0][2] * matriz_det2[1][1] * matriz_det2[2][0]

resultado_diag_s = diag_s1+diag_s2+diag_s3

resultado_matriz_2 = resultado_diag_p - resultado_diag_s

print(f"Resultado: {resultado_diag_p} - {resultado_diag_s} = {resultado_matriz_2}")
