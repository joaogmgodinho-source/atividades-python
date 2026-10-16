#  Exercício 18 — Maior ou iguais
#  Aluno: João Gustavo
#  Objetivo: Leia dois números e mostre qual é o maior. Se forem iguais, mostre Os números são iguais.

# Pede o primeiro número
n1 = int(input("Digite o primeiro número: "))

# Pede o segundo número
n2 = int(input("Digite o segundo número: "))

# Compara se o primeiro número é maior que o segundo
if n1 > n2:
    print(f"{n1} é maior que {n2}")
# Compara se o primeiro número é igual ao segundo
elif n1 == n2:
    print("Os números são iguais")
# Se nenhum dos dois de cima forem verdade, o segundo é maior que o primeiro
else:
    print(f"{n2} é maior que {n1}")
