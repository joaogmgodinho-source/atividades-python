#  Exercício 34 — Aprovação com frequência
#  Aluno: João Gustavo
#  Objetivo: Para ser aprovado, o aluno precisa de média maior ou igual a 7.0 e frequência de pelo menos 75%. Leia duas
# notas e a frequência (em %) e mostre:
# • Reprovado por falta, se a frequência for menor que 75% (mesmo com nota boa);
# • Reprovado por nota, se a frequência estiver ok mas a média for menor que 7.0;
# • Aprovado, se as duas condições forem atendidas.

# Pede a primeira nota
n1 = float(input("Digite a primeira nota: "))

# Pede a segunda nota
n2 = float(input("Digite a segunda nota: "))

# Faz a conta para descobrir a média
media = (n1 + n2) / 2.0

# Pede a frequencia
frequencia = int(input("Digite a frequencia: "))

# Mostra que está aprovado se as duas condições forem atendidas
if media >= 7.0 and frequencia >= 75:
    print("Aprovado")
# Mostra reporvado por nota se a frequência estiver ok mas a média for menor que 7.0
elif media < 7.0 and frequencia >= 75:
    print("Reprovado por nota")
# Mostra reprovado por falta se a frequência for menor que 75% (mesmo com nota boa)
elif media >= 7.0 and frequencia < 75:
    print("Reprovado por falta")