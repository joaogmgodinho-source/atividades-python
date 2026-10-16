# Exercício 10 — Aprovado ou reprovado
# Aluno: João Gustavo
# Objetivo: Leia duas notas de um aluno e calcule a média. Mostre a média e a mensagem Aprovado se ela for maior ou
# igual a 7.0, ou Reprovado caso contrário.

# Pede para digitar a primeira nota e guarda na variavel
nota1 = float(input("Digite a primeira nota: "))

# Pede para digitar a segunda nota e guarda na variavel
nota2 = float(input("Digite a segunda nota: "))

# Faz a conta para a média
media = (nota1 + nota2) // 2.0

# Mostra sua média
print(f"A sua média é: {media}")

# Compara se a média é maior ou igual a 7, e mostra se ta aprovado ou reprovado
if media >= 7.0:
    print("Aprovado")
else:
    print("Reprovado") 
