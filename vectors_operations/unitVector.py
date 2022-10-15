from math import *

'''class Versor(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def getVersor(self):
        den = pow((self.x**2 + self.y**2 + self.z**2), 1/2)
        u =  1 / den
        
        print("1/{:.2f}" .format(den))
        
    def __str__(self):
        return f'1/{3} ({self.x:.2f}, {self.y:.2f}, {self.z:.2f})' '''


def versor(u):
    mod_u = 0
    value = 0
    v = []
    
    for i in range(3):
        mod_u = mod_u + u[i]*u[i]
    
    mod_u = pow(mod_u, 1/2)
    for i in range(3):
        value = (1 / mod_u) * u[i]
        v.append(value) 
    
    print(f'Versor: 1/{mod_u:.2f} ({u[0]:.2f}, {u[1]:.2f}, {u[2]:.2f})')
    print(f'Versor: ({v[0]:.2f}, {v[1]:.2f}, {v[2]:.2f})')


u = []

print("Versor de um Vetor: ")
print("Coordenadas do vetor: ")
for i in range(3):
    u.append(float(input("Digite a %da. coordenada: " %(i+1) )))

versor(u)

        