# Exercício 14 — Radar de velocidade
# Aluno: João Gustavo
# Objetivo: Numa via com limite de 80 km/h, leia a velocidade de um carro. Se ele passou do limite, mostre quantos
# km/h acima ele estava. Senão, mostre Velocidade dentro do limite. Boa viagem!

# Pede a velocidade do carro
velocidade = int(input("Digite a velocidade: ")) 

# Compara se a velocidade passou do limite, se sim, mostrs que está multado e tambem, 
# o quanto foi passado do limite, se nao, Mostra boa viagem
if velocidade > 80:
    print(f"Multado! você passou {velocidade - 80} km/h do limite")
else:
    print("Velocidade dentro do limite. Boa viagem!")
    
    
