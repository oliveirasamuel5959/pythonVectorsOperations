import math


def ortogonal_pjr(u, v):
    mod_u = 0
    mod_v = 0
    escalar = 0
    pjr = 0
    mult_vector = 0
    pjr_uv = []
    
    #Calculo do modulo v
    for i in range(3):
        mod_v = mod_v + v[i]*v[i]
    
    #produto escalar entre u e v
    for i in range(3):
        escalar += u[i]*v[i]
    
    pjr = escalar / mod_v
    
    for i in range(3):
        mult_vector = v[i] * pjr
        pjr_uv.append(mult_vector)
    
    print(f'Projeção Ortogonal: {escalar:.2f}/{mod_v:.2f}({v[0]:.2f}, {v[1]:.2f}, {v[2]:.2f})')
    print(f'Projeção Ortogonal: ({pjr_uv[0]:.2f}, {pjr_uv[1]:.2f}, {pjr_uv[2]:.2f})')
    

u = []
v = []

print("Projeção Ortogonal do vetor u sobre o vetor v: ")
print("Coordenadas do vetor u: ")
for i in range(3):
    u.append(float(input("Digite a %da. coordenada: " %(i+1) )))
    
print("Coordenadas do vetor v: ")
for i in range(3):
    v.append(float(input("Digite a %da. coordenada: " %(i+1) )))

ortogonal_pjr(u, v)

        