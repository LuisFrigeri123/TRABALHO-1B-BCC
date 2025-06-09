################# MATRIZ SIMILARIDADE ###########################
################################################################################################################################
matriz_dataset = []

# Formatando a lista
with open("dataset.txt", "r") as dataset:
    for linha in dataset:
        matriz_dataset.append(linha.replace('"', "").replace(
            "[", "").replace("'", "").replace("]", "").replace("\n", "").split(","))

# Removendo bandas repetidas
bandas = []
for linha in matriz_dataset:
    bandas.append(linha[1].strip())
    bandas.append(linha[2].strip())
    bandas.append(linha[3].strip())
for banda in bandas:
    if bandas.count(banda) >= 2:
        bandas.remove(banda)

# Adicionando as bandas à matriz de similaridade
with open("matriz_sim.txt", "a+") as similaridade:
    similaridade.write("+,")
    for banda in bandas:
        similaridade.write(f"{banda.strip()},")
    similaridade.write("\n")

matriz_similaridade = []
# Adicionando os nomes dos alunos e criando a matriz similaridade
with open("matriz_sim.txt", "a+") as similaridade:
    for linha in matriz_dataset:
        zero_um = []
        similaridade.write(linha[0].strip() + ",")
        for banda in bandas:
            if banda.lower().strip() == linha[1].lower().strip() or banda.lower().strip() == linha[2].lower().strip() or banda.lower().strip() == linha[3].lower().strip():
                similaridade.write("1,")
                zero_um.append("1")
            else:
                similaridade.write("0,")
                zero_um.append("0")
        similaridade.write("\n")
        matriz_similaridade.append(zero_um)
####################################################################################################################################
####################################################################################################################################


while True:
    print("\nEscolha o que deseja utilizar:")
    print("0 - Sair")
    print("1 - Visualizar matriz similaridade")
    print("2 - Visualizar bandas favoritas de um aluno")
    print("3 - Visualizar quantas vezes uma banda foi escolhida")
    escolha = input("\n")

    if escolha == "0":
        print("")
        break

    elif escolha == "1":
        print("")
        for linha in matriz_similaridade:
            print(["".join(linha)])
        print("")

    elif escolha == "2":
        print("")
        nome_aluno = input("Digite o nome do(a) aluno(a): ")
        print("")
        for linha in matriz_dataset:
            if linha[0].strip().lower() == nome_aluno.strip().lower():
                print(linha[0])
                print(
                    f"As bandas favoritas do(a) {nome_aluno} são: {linha[1]}, {linha[2]} e {linha[3]}\n")

    elif escolha == "3":
        print("")
        nome_banda = input("Digite o nome da banda: ")
        qtdade = 0
        for linha in matriz_dataset:
            if linha[1].strip().lower() == nome_banda.strip().lower() or linha[2].strip().lower() == nome_banda.strip().lower() or linha[3].strip().lower() == nome_banda.strip().lower():
                qtdade += 1
        print(f"\nA banda {nome_banda} foi citada {qtdade} vezes\n")

    else:
        print("\nVocê digitou um valor inválido\n")
