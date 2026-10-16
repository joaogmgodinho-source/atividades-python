# Exercício 4 — Celsius para Fahrenheit
# Aluno: João Gustavo
# Objetivo: Leia uma temperatura em graus Celsius e mostre o valor em Fahrenheit. Fórmula: F = C × 1.8 + 32.

# Pede os graus em celsius para transformar em fahrenheit
celsius = float(input("Digite a temperatura em celsius para transformar em fahrenheit: "))

# Transforma os celsius em fahrenheit
fahrenheit = celsius * 1.8 + 32

# Mostra o resultado na tela
print(f"A temperatura em fahrenheit é: {fahrenheit} °F")