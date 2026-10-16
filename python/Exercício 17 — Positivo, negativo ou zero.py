#  Exercício 17 — Positivo, negativo ou zero
#  Aluno: João Gustavo
#  Objetivo: Leia um número e informe se ele é positivo, negativo ou zero.

# Pede um número
n1 = int(input("Digite um número: "))

# Compara se o número é maior que zero, ou seja positivo
if n1 > 0:
    print("O seu número é positivo")
# Compara se o número é igual a zero, ou seja zero
elif n1 == 0:
    print("O seu número é zero")
# Compara se o número digitado é menor que zero, ou seja negativo
else:
    print("O seu número é negativo")
