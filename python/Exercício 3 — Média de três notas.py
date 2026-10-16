# Exercício 3 — Média de três notas
# Aluno: João Gustavo
# Objetivo: Leia três notas (podem ter casas decimais) e mostre a média aritmética.

# Pede a primeira nota e guarda na variavel nota1
nota1 = float(input("Digite a primera nota: "))

# Pede a segunda nota e guarda na variavel nota2
nota2 = float(input("Digite a segunda nota: "))

# Pede a terceira nota e guarda na variavel nota3
nota3 = float(input("Digite a terceira nota: "))

# Mostra o resultado da média na tela
print(f"Sua média é: {(nota1 + nota2 + nota3) // 3.0}")