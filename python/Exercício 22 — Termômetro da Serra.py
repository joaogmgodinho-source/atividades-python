#  Exercício 22 — Termômetro da Serra
#  Aluno: João Gustavo
#  Objetivo: Leia a temperatura do dia em °C (pode ter casas decimais) e mostre a mensagem conforme a tabela.

# Pede a temperatura
temperatura = float(input("Digite a temperatura: "))

# Compara se a temperatura é menor que zero
if temperatura < 0:
    print("Abaixo de zero - risco de geada")
# Compara se a temperatura é menor que 10
elif temperatura < 10:
    print("Muito frio — capriche no agasalho")
# Compara se a temperatura é menor que 18
elif temperatura < 18:
    print("Frio")
# Compara se a temperatura é menor ou igual a 25
elif temperatura <= 25:
    print("Agradavel")
# Compara se a temperatua é maior que 25
elif temperatura > 25:
    print("Calor")