#  Exercício 39 — Caixa eletrônico: contagem de notas
#  Aluno: João Gustavo
#  Objetivo: Um caixa eletrônico tem notas de R$ 100, R$ 50, R$ 20 e R$ 10. Leia o valor do saque (número inteiro) e
# mostre a menor quantidade de notas para pagá-lo.
# • Se o valor for menor ou igual a zero, ou não for múltiplo de 10, mostre Valor inválido para
# saque.
# • Mostre apenas as notas que forem usadas (quantidade maior que zero).

# Pede o valor do saque
saque = int(input("Digite o valor do saque: "))

# Compara se o saque é menor ou igual a 0 ou se o saque não é multiplo de 10 mostra saque invalido e termina o sistema
if saque <= 0 or saque % 10 != 0:
    print("Valor inválido para o saque")
# Continua o sistema
else:

    # Faz essa conta para descobrir quantas notas de 100 são precisas
    quantidade = saque // 100

    # Se não precisar de notas de 100, não mostra
    if quantidade > 0:
        print(f"Quantidade de notas de R$ 100: {quantidade}")
    # Faz essa conta para descontar no valor do saque para descontar a conta
    saque = saque % 100        

    # Faz essa conta para descobrir quantas notas de 50 são precisas
    quantidade = saque // 50

    # Se não precisar de notas de 50, não mostra
    if quantidade> 0:
        print(f"Quantidade de notas de R$ 50: {quantidade}")
    # Faz essa conta para descontar no valor do saque para descontar a conta
    saque = saque % 50   

    # Se não precisar de notas de 20, não mostra
    quantidade = saque // 20

    # Se não precisar de notas de 20, não mostra
    if quantidade> 0:
        print(f"Quantidade de notas de R$ 20: {quantidade}")
    # Faz essa conta para descontar no valor do saque para descontar a conta
    saque = saque % 20

    # Se não precisar de notas de 10, não mostra
    quantidade = saque // 10

    # Se não precisar de notas de 10, não mostra
    if quantidade> 0:
        print(f"Quantidade de notas de R$ 10: {quantidade}")
    # Faz essa conta para descontar no valor do saque para descontar a conta
    saque = saque % 10 




