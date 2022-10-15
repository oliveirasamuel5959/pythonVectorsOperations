def escalarProd(u, v, len):
    sum = 0
    
    for i in range(len):
        sum = sum + u[i]*v[i]
    
    return sum

print("Produto Escalar: ")
len = int(input("Digite a dimensão dos vetores: "))

u = []
v = []

print("Coordenadas do vetor u: ")
for i in range(len):
    u.append(float(input("Digite a %da. coordenada: " %(i+1) )))
    
print("Coordenadas do vetor v: ")
for i in range(len):
    v.append(float(input("Digite a %da. coordenada: " %(i+1) )))

result = escalarProd(u, v, len)

print("Produto Escalar: {:.2f}" .format(result))