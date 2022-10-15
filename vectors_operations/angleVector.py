import math


def dot_angle(u, v):
    mod_u = 0
    mod_v = 0
    escalar = 0
    theta = 0
    degree = 0
    cos_theta = 0
    
    #Calculo do modulo de u e v
    for i in range(3):
        mod_u = mod_u + u[i]*u[i]
        mod_v = mod_v + v[i]*v[i]
        
    mod_u = pow(mod_u, 1/2)
    mod_v = pow(mod_v, 1/2)
    
    #produto escalar entre u e v
    for i in range(3):
        escalar += u[i]*v[i]
    
    
    cos_theta = escalar / (mod_u * mod_v)
    
    theta = math.acos(cos_theta)
    
    theta = theta * (180/math.pi)
    
    print(f'Ângulo: {theta:.2f} graus')
    

u = []
v = []

print("Ângulo entre os vetores u e v: ")
print("Coordenadas do vetor u: ")
for i in range(3):
    u.append(float(input("Digite a %da. coordenada: " %(i+1) )))
    
print("Coordenadas do vetor v: ")
for i in range(3):
    v.append(float(input("Digite a %da. coordenada: " %(i+1) )))

dot_angle(u, v)

        