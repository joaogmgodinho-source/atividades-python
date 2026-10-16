# Exercício 15 — Desconto na compra
# Aluno: João Gustavo
# Objetivo: Uma loja dá 10% de desconto em compras a partir de R$ 100,00. Leia o valor da compra e mostre o valor
# final a pagar.

# Pede para digitar o valor da compra
valor = float(input("Digite o valor da compra: "))

# Compara se o valor da compra é maior que 100, se sim, aplica um desconto
if valor >= 100:
    desconto = valor * 0.10
    total = valor - desconto
else:
    total = valor

# Mostra o valor total a se pagar
print(f"O valor a se pagar é: {total}")