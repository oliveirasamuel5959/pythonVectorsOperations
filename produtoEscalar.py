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

print("Vetor Soma: (", end="")
for index in range(len(vetor_resultado)):
    print(f"{vetor_resultado[index]:.2f}, ", end=None)
print(end=")")
