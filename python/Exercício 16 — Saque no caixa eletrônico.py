# Exercício 16 — Saque no caixa eletrônico
# Aluno: João Gustavo
# Objetivo: Leia o saldo da conta e o valor que a pessoa quer sacar. Se houver saldo suficiente, mostre o novo saldo.
# Senão, mostre Saldo insuficiente.

# Pede o saldo disponivel
saldo = float(input("DIgite o seu saldo: "))

# Pede o quanto quer sacar
saque = float(input("Digite o quanto você quer sacar: "))

# Compara se o saldo é suficiente para o saque, se sim, faz o saque e mostra o novo saldo
if saque > saldo:
    print("Saldo insuficiente")
else:
    saldo = saldo - saque
    print(f"Saque realizado - Novo saldo: {saldo}")