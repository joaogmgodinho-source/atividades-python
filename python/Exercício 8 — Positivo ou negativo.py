# Exercício 8 — Positivo ou negativo
# Aluno: João Gustavo
# Objetivo: Leia um número inteiro e informe se ele é positivo ou negativo. Neste exercício, considere o zero como
# positivo.

# Pede um número e guarda na variavel
n = int(input("Digite um número: "))

# Compara se esse número é menor que 0, se sim, 
# mostra que ele negativo, se não, motra que ele é positivo
if n < 0:
    print(f"{n} é negativo")
else:
    print(f"{n} é positivo")