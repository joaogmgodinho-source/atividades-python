#  Exercício 33 — Voto obrigatório
#  Aluno: João Gustavo
#  Objetivo: Leia a idade de uma pessoa e informe a situação dela nas eleições brasileiras:

# Pede a idade
idade = int(input("Digite sua idade: "))

# Compara se tem menos de 16 (não pode votar)
if idade < 16:
    print("Não pode votar")
# Compara se entre 16 e 17, ou maior de 70 (voto facultativo)
elif idade >=16 and idade <= 17 or idade > 70:
    print("Voto facultativo")
# Compara se esta entre 18 e 70 (voto obrigatorio)
elif idade >= 18 and idade <= 70:
    print("Voto obrigatório")