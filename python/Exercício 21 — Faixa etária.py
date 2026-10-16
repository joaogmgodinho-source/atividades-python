#  Exercício 21 — Faixa etária
#  Aluno: João Gustavo
#  Objetivo: Leia a idade de uma pessoa e mostre a faixa etária conforme a tabela.

# Pede a idade
idade = int(input("Digite sua idade: "))

# Faz todas as comparações para mostras a faixa etaria
if idade < 0:
    print("Idade invalida")
elif idade < 13:
    print("Criança")
elif idade < 18:
    print("Adolescente")
elif idade < 60:
    print("Adulto")
elif idade >= 60:
    print("Idoso")