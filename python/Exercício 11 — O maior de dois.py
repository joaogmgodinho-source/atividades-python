# Exercício 11 — O maior de dois
# Aluno: João Gustavo
# Objetivo: Leia dois números diferentes e mostre qual deles é o maior.

# Pede para digitar o primeiro número para comparar
n1 = int(input("Digite o primeiro número: "))

# Pede para digitar o segundo número para comparar
n2 = int(input("Digite o segundo número: "))

# Compara se o primeiro é maior que o segundo, e mostra qual o maior
if n1 > n2:
    print(f"{n1} é maior que {n2}")
else:
    print(f"{n2} é maior que {n1}")