#  Exercício 38 — Equação do 2º grau
#  Aluno: João Gustavo
#  Objetivo: Leia os coeficientes a, b e c de uma equação ax² + bx + c = 0 e resolva:
# • Se a for zero, mostre Não é uma equação do 2º grau.
# • Calcule delta: Δ = b² − 4 × a × c.
# • Se Δ < 0, mostre Não existem raízes reais.
# • Se Δ = 0, existe uma raiz: x = −b ÷ (2 × a).
# • Se Δ > 0, existem duas raízes: x1 = (−b + √Δ) ÷ (2 × a) e x2 = (−b − √Δ) ÷ (2 × a).
# Raiz quadrada: no Portugol Studio, escreva inclua biblioteca Matematica --> mat logo abaixo
# de programa { e use mat.raiz(delta, 2.0). No Python, use delta ** 0.5.


# Pede o coeficiente A
a = int(input("Digite o coeficiente A: "))

# Pede o coeficiente B
b = int(input("Digite o coeficiente B: "))

# Pede o coeficiente C
c = int(input("Digite o coeficiente C: "))

# Compara se o A é igual a 0, se sim ele da erro e para o sistema
if a == 0:
    print("Erro: coeficiente A não pode ser igual a 0")
# Continua o sistema
else:

    # Faz a conta do delta
    delta = b**2 - 4 * a * c

    # Compara se o delta é igual a zero, se sim ele fala que não tem raiz e para o sistema
    if delta < 0:
        print("Não existe raiz")
    # Compara se o delta é igual a zero, se sim, so tem uma raiz e continua a conta
    elif delta == 0:
        
        # Mostra que so tem uma raiz
        print("Existe uma raiz")

        # Faz a conta do X
        x = -b / (2 * a)

        # Mostra o resultado
        print(f"O resultado é: {x}")
    
    # Compara se o delta é maior que zero, se sim, ele fala que tem 2 raizes e continua a conta
    elif delta > 0:

        # Mostra que tem 2 raizes
        print("Existe 2 raizes")

        # Faz a conta do x1
        x1 = (-b + delta**0.5) / (2 * a) 

        # Faz a conta do x2
        x2 = (-b - delta**0.5) / (2 * a)

        # Mostra os 2 resultados
        print(f"O resultado é: x1: {x1}, x2: {x2}")



