# Exercício 9 — Par ou ímpar
# Aluno: João Gustavo
# Objetivo: Leia um número inteiro e informe se ele é par ou ímpar.

# Pede para digitar o número
n = int(input("Digite um número: "))

# Compara se o resto da divisão do número por 2 é igual a 0, se sim, mostra que é par, se não, motra que ímpar
if n % 2 == 0:
    print(f"{n} é par")
else:
    print(f"{n} é ímpar")