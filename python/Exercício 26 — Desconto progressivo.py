#  Exercício 26 — Desconto progressivo
#  Aluno: João Gustavo
#  Objetivo: Leia o valor de uma compra e aplique o desconto da faixa correspondente. Mostre o valor do desconto e o
#  valor final.

# Pede para digitar o valor da compra
valor = float(input("Digite o valor da compra: "))

# Compara de o valor é menor que 50, se sim, não da desconto
if valor < 50:
    desconto = 0
    final = valor - desconto
# Compara se o valor é menor que 100, se sim, da desconto de 5%
elif valor < 100:
    desconto = valor * 0.5
    final = valor - desconto
# Compara se o valor é menor que 200, se sim, da desconto de 10% 
elif valor < 200:
    desconto = valor * 0.10
    final = valor - desconto
# Compara se o valor é maior ou igual a 200, se sim, da desconto de 15%
elif valor >= 200:
    desconto = valor * 0.15
    final = valor - desconto

# Mostra o resultado
print(f"Desconto: R$ {desconto} - final: R$ {final}")

