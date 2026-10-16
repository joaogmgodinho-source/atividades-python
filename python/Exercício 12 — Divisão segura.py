# Exercício 12 — Divisão segura
# Aluno: João Gustavo
# Objetivo: Leia dois números: o dividendo e o divisor. Se o divisor for zero, mostre Erro: não existe divisão
# por zero. Caso contrário, mostre o resultado da divisão.

# Pede o dividendo 
dividendo = float(input("Digite o dividendo (número que vai ser dividido): "))

# Pede o divisor
divisor = float(input("Digite o divisor (número que vai dividir): "))

# Compara se o divisor é igual a 0, se sim, aparece erro, se não, ele faz a divisão e mostra
if divisor == 0:
    print("Erro: não existe divisão por zero")
else:
    print(f"Resultado: {dividendo / divisor}")