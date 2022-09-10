

from posixpath import split


def somaVector(u,v):
    uv_sum = []
    for i in range(3):
        uv_sum.append(u[i] + v[i])
    return uv_sum

vetor_resultado = []
print("Soma de Vetores")

print("Coordenadas do vetor u:")
u = []
for i in range(3):
    u.append(float(input("Digite a %da. coordenada: " %i)))

print("Coordenadas do vetor v:")
v = []
for i in range(3):
    v.append(float(input("Digite a %da. coordenada: " %i)))

vetor_resultado = somaVector(u,v)

print("Vetor Soma: (", end="")
for index in range(len(vetor_resultado)):
    print(f"{vetor_resultado[index]:.2f}, ", end=None)
print(end=")")