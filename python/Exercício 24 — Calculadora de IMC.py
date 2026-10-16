#  Exercício 24 — Calculadora de IMC
#  Aluno: João Gustavo
#  Objetivo: Leia o peso (kg) e a altura (m) de uma pessoa. Calcule o IMC = peso ÷ (altura × altura) e mostre a
# classificação

# Pede o para digitar o peso
peso = float(input("Digite seu peso (Kg): "))

# Pede para digitar a altura
altura = float(input("Digite sua altura: "))

# Faz a formula para descobrir o IMC
imc = peso / (altura * altura)

# Mostra o IMC
print(f"IMC: {imc}")

#  Compara se o IMC é menor que 18.5, 25, 30, ou maior que 30, de acordo com isso ele fala
#  se está Abaixo do peso, peso normal, etc
if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso normal")
elif imc < 30:
    print("Sobrepeso")
elif imc >= 30:
    print("Obesidade")