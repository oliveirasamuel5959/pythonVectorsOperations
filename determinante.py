ordem = int(input("Digite a ordem da matriz (até ordem 3)"))


def det(m):
    detM = 0
    if(len(m) == 3):
        detM = detM + m[0][0]*(m[1][1]*m[2][2] - m[1][2]*m[2][1])
        detM = detM - m[0][1]*(m[1][0]*m[2][2] - m[1][2]*m[2][0])
        detM = detM + m[0][2]*(m[1][0]*m[2][1] - m[1][1]*m[2][0])
        return print(detM)

    if(len(m) == 2):
        detM = detM + m[0][0]*m[1][1] - m[0][1]*m[1][0]
        return print(detM)
    
    if(len(m) == 1):
        return print(m[0][0])
M = []

for num_linha in range(ordem):
    linha = []
    for num_coluna in range(ordem):
        linha.append(float(input("Digite o elemento %d %d da matriz: " %(num_linha+1, num_coluna+1))))
    M.append(linha)
print()

det(M)



