

num_linhas = int(input("Digite o número de linhas da matriz M: "))
num_colunas = int(input("Digite o número de colunas da matriz M: "))

m_transposta = []

def transposta(m):
    for i in range(num_colunas):
        lista = []
        for j in range(num_linhas):
            lista.append(m[j][i])
        m_transposta.append(lista)

    return m_transposta


M = []
result = []
for i in range(num_linhas):
    linha = []
    for j in range(num_colunas):
        linha.append(float(input("Digite o elemento %d %d da matriz: " %(i+1, j+1))))
    M.append(linha)
print("Matriz")

for i in range(len(M)):
    for j in range(len(M[i])):
        print(M[i][j], end=" ")
    print()

print()
print("MATRIZ TRANSPOSTA:")
result = transposta(M)
for i in range(len(result)):
    for j in range(len(result[i])):
        print(result[i][j], end=" ")
    print()