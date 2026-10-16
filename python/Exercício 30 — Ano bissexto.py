#  Exercício 30 — Ano bissexto
#  Aluno: João Gustavo
#  Objetivo: Leia um ano e informe se ele é bissexto. Um ano é bissexto quando é divisível por 4 e não é divisível por
#  100, ou quando é divisível por 400.

# Pede para digitar o ano
ano = int(input("Digite um ano, para ver se ele é bissexto: "))

# Compara se o ano é divisível por 4 e não é divisível por
# 100, ou quando é divisível por 400.
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Bissexto")
else:
    print("Não é bissexto")