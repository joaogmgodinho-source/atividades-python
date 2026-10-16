#  Exercício 25 — Radar com tipo de infração
#  Aluno: João Gustavo
#  Objetivo: Leia o limite de velocidade da via e a velocidade medida do carro. Calcule quantos por cento a velocidade
# passou do limite e classifique conforme a tabela.

# Pede para digitar o limite da velocidade
limite = float(input("Digite o limite da velocidade: "))

# Pede para digitar a velocidade do carro
velocidade = float(input("Digite a velocidade do carro: "))

# Faz a conta para pegar o percentual
percentual_acima = (velocidade - limite) / limite * 100

# Compara o quanto a velocidade passou do limite e mostra qual infração teve
if velocidade <= limite:
    print("Sem infração")
elif percentual_acima < 20:
    print(f"{percentual_acima} acima - infração média")
elif percentual_acima <= 50:
    print(f"{percentual_acima} acima - infração grave")
elif percentual_acima > 50:
    print(f"{percentual_acima} acima - infração gravissima")