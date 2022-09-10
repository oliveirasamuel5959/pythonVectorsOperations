
'''========== Código para entrar com o número de linhas e colunas da matrix M =============='''
M = []

print("ADIÇÃO DE MATRIZES:")
linhas_m = int(input('Digite o número de linhas  da matriz M: '))
colunas_m = int(input('Digite o número de colunas da matriz M: '))

for num_linha in range(linhas_m):
    linha = []
    for num_coluna in range(colunas_m):
        linha.append(float(input("Digite o elemento %d %d da matriz: " %(num_linha+1, num_coluna+1))))
    M.append(linha)
print()

'''for linha in range(len(M)):
    for coluna in range(len(M[linha])):
        print("%d" %M[linha][coluna], end=" ")'''



    

'''========== Código para entrar com o número de linhas e colunas da matrix N =============='''
N = []


linhas_n = int(input('Digite o número de linhas  da matriz N: '))
colunas_n = int(input('Digite o número de colunas da matriz N: '))

for num_linha in range(linhas_n):
    linha = []
    for num_coluna in range(colunas_n):
        linha.append(float(input("Digite o elemento %d %d da matriz: " %(num_linha+1, num_coluna+1))))
    N.append(linha)

'''for linha in range(len(N)):
    for coluna in range(len(N[linha])):
        print("%d" %N[linha][coluna], end=" ")'''



matriz_soma = []

if linhas_m != linhas_n:
    print("Matrizes Incompatíveis.")
else:
    for i in range(linhas_m):
        linha = []
        for j in range(colunas_n):
            linha.append(M[i][j] + N[i][j])
        matriz_soma.append(linha)
    #print()

    for i in range(len(matriz_soma)):
        for j in range(len(matriz_soma[i])):
            print("%.1f" %matriz_soma[i][j], end=" ")
        print()


