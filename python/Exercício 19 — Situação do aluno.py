#  Exercício 19 — Situação do aluno
#  Aluno: João Gustavo
#  Objetivo: Leia duas notas, calcule a média e mostre a situação do aluno conforme a tabela.

# Pede a primeira nota
n1 = float(input("Digite a primeira nota: "))

# Pede a segunda nota
n2 = float(input("Digite a segunda nota: "))

# Faz a conta para descobrir a média
media = (n1 + n2) / 2.0

# Mostra o resultado da média
print(f"A sua média é: {media}")

# Compara qual foi a média e mostra a situação do aluno
if media >= 7.0:
    print("Situação: Aprovado")
elif media >= 5:
    print("Situação: Recuperação")
else:
    print("Situação: Reprovado")