# Exercício 5 — Minutos em horas
# Aluno: João Gustavo
# Objetivo: Leia uma quantidade de minutos (número inteiro) e mostre quantas horas e quantos minutos ela representa.

# Pede o número em minutos
n1 = int(input("Digite uma quantidade de minutos para tranformar em minutos e horas: "))

# Faz a conta para descobrir as horas
horas = n1 // 60

# Faz a conta para descobrir os minutos
minutos = n1 % 60

# Mostra eles na tela
print(f"{horas} horas e {minutos}")
