# Exercício 6 — Compra na cantina
# Aluno: João Gustavo
# Objetivo: Leia o preço de um lanche, a quantidade comprada e o valor que o cliente pagou. Mostre o total da compra e
# o troco. Considere que o valor pago é sempre suficiente.

# Pede o preco do lanche
preco = float(input("Digite o preço do lanche: "))

# Pede a quantidade que foi pedida
quantidade = int(input("Digite a quantidade: "))

# Pede o valor que o cliente pagou
valor_pago = float(input("DIgite o valor pago: "))

# Faz a conta para conseguir o valor total
total = preco * quantidade

# Mostra o quanto de troco deve ser devolvido
print(f"Deve ser devolvido R$ {valor_pago - total} de troco")



