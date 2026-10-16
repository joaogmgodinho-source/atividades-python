#  Exercício 23 — Cardápio da cantina
#  Aluno: João Gustavo
#  Objetivo: Mostre o cardápio abaixo na tela, leia o código do produto e a quantidade, e mostre o total a pagar. Se o
# código não existir, mostre Código inválido.

# Mostra o cardapio
print(" Código |    Produto    | Preço ")
print("    1   | pão de queijo | 4,50 ")
print("    2   |    coxinha    | 6,00 ")
print("    3   |    pastel     | 7,00 ")
print("    4   |     Suco      | 5,00 ")
print("    5   |     café      | 3,00 ")

# Pede o codigo do produto
codigo = int(input("Digite o codigo do produto: "))

# Pede a quantidade
quantidade = int(input("Digite a quantidade: "))

# compara qual codigo é do produto e faz a conta, e mostra o preco total
if codigo == 1:
    print("Pão de queijo")
    total = 4.50 * quantidade
    print(f"Total: R$ {total}")
elif codigo == 2:
    print("Coxinha")
    total = 6.00 * quantidade
    print(f"Total: R$ {total}")
elif codigo == 3:
    print("Pastel")
    total = 7.00 * quantidade
    print(f"Total: R$ {total}")
elif codigo == 4:
    print("Suco")
    total = 5.00 * quantidade
    print(f"Total: R$ {total}")
elif codigo == 5:
    print("Café")
    total = 3.00 * quantidade
    print(f"Total: R$ {total}")
else:
    print("Código inválido")