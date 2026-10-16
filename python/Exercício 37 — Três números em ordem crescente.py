#  Exercício 37 — Três números em ordem crescente
#  Aluno: João Gustavo
#  Objetivo: Leia três números diferentes e mostre-os em ordem crescente. Não use listas nem funções prontas de
# ordenação: resolva apenas com se / senao se / senao.

# Pede o primeiro número
n1 = int(input("Digite o primeiro número: "))

# Pede o segundo número
n2 = int(input("Digite o segundo número: "))

# Pede o terceiro número
n3 = int(input("Digite o terceiro número: "))

# Faz todas as 6 possibilidades das ordens crescentes
if n1 <= n2 and n2 <= n3:
    print(f"Crescente: {n1} {n2} {n3}")
elif n1 <= n3 and n3 <= n2:
    print(f"Crescente: {n1} {n3} {n2}")
elif n2 <= n1 and n1 <= n3:
    print(f"Crescente: {n2} {n1} {n3}")
elif n2 <= n3 and n3 <= n1:
    print(f"Crescente: {n2} {n3} {n1}")
elif n3 <= n1 and n1 <= n2:
    print(f"Crescente: {n3} {n1} {n2}")
else:
    print(f"Crescente: {n3} {n2} {n1}")
