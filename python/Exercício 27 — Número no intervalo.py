#  Exercício 27 — Número no intervalo
#  Aluno: João Gustavo
#  Objetivo: Leia um número inteiro e informe se ele está entre 1 e 100, incluindo o 1 e o 100.

# Pede para digitar o número
n = int(input("Digite um número para comparar que está dentro de 1 e 100: "))

# Compara se ele está dentro do intervalo de 1 e 100
if n >= 1 and n <= 100:
    print("Dentro do intervalo")
else:
    print("Fora do intervalo")