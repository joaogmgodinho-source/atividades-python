# Exercício 7 — Maior ou menor de idade
# Aluno: João Gustavo
# Objetivo: Leia a idade de uma pessoa e informe se ela é maior de idade (18 anos ou mais) ou menor de idade.

# Pede a idade e guarda na variavel idade 
idade = int(input("Digite a sua idade: "))

# compara se a idade é maior de 18, se sim, mostra que é maior de idade, se não, mostra que é menor de idade
if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")    