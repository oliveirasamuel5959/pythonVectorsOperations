from imaplib import Int2AP
from sys import flags


def escalarProd(u, k):
    for i in range(len(u)):
        u[i] = k*u[i]
    return u

vetor_resultado = []

print("Multiplicação de Escalar Real por Vetor: ")
print("Coordenadas do Vetor u: ")
u = []
for i in range(3):
    u.append(float(input("Digite a %da. coordenada: " %(i+1))))
k = float(input("Digite o valor de k: "))


vetor_resultado = escalarProd(u, k)
vetor_rounded = [ '%.2f' % elem for elem in vetor_resultado ]

'''print("Vetor: (", end="")
for index in range(len(vetor_resultado)):
    print(f"{vetor_resultado[index]:.2f}, ", end="")
print(")")'''

print("Vetor: (", end="")
print(', '.join(map(str, vetor_rounded)), end="")
print(")", end="")


