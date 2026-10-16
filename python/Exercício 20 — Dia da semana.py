#  Exercício 20 — Dia da semana
#  Aluno: João Gustavo
#  Objetivo: Leia um número de 1 a 7 e mostre o dia da semana correspondente (1 = Domingo, 2 = Segunda-feira, … 7 =
# Sábado). Para qualquer outro número, mostre Dia inválido.

# Pede o número para representar o dia
n1 = int(input("Digite um número para representar um dia da semana (1 a 7): "))

# Faz todas as comparações dos dias, para o número representar o dia
if n1 == 1:
    print("Domingo")
elif n1 == 2:
    print("Segunda-feira")
elif n1 == 3:
    print("Terça-feira")
elif n1 == 4:
    print("Quarta-feira")
elif n1 == 5:
    print("Quinta-feira")
elif n1 == 6:
    print("Sexta-feira")
elif n1 == 7:
    print("Sábado")
else:
    print("Dia inválido")