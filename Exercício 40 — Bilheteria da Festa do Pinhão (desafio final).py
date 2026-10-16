#  Exercício 40 — Bilheteria da Festa do Pinhão (desafio final)
#  Aluno: João Gustavo
#  Objetivo: Simule a venda de um ingresso para a Festa do Pinhão (valores fictícios). O ingresso inteiro custa R$ 40.00.
# 1. Leia a idade do comprador e se ele é estudante (s ou n).
# 2. Defina o tipo de ingresso:
#   – menos de 6 anos: Gratuito (R$ 0.00);
#   – de 6 a 17 anos, 60 anos ou mais, ou estudante: Meia-entrada (R$ 20.00);
#   – todos os outros casos: Inteira (R$ 40.00).
# 3. Se o ingresso for gratuito, mostre Gratuito — R$ 0.0 e encerre, sem pedir pagamento.
# 4. Senão, leia a forma de pagamento: 1 = PIX (5% de desconto), 2 = Débito (sem alteração), 3 = Crédito
# (5% de acréscimo). Para qualquer outro código, mostre Forma de pagamento inválida.
# 5. Mostre o resumo: tipo de ingresso, forma de pagamento e valor final.

# pede a idade
idade = int(input("Digite sua idade: "))

# Compara se a idade é menor que 6 se sim, a entrada é de graça e termina o sistema
# se não, continua o sistema
if idade < 6:
    print("Gratuito - R$: 0.00")
else:

    # Pergunta se é estudante
    estud = input("Você é estudante? (sim/não): ")

    # Para meia entrada, verifica se a idade está entre 6 e 17, se a idade é maior que 60, ou é estudante
    if (idade <= 6 and idade <= 17) or (idade > 60) or (estud == "sim"):

        valor = 20.00

        entrada = "Meia-entrada"
    
    # se nenhum das condições forem verdadeiras, da entrada inteira
    else:

        valor = 40.00

        entrada = "Inteira"

    # Pede a forma de pagamento
    pagamento = input("Coloque a forma de pagamento (PIX | débito | crédito): ")

    # PIX: da 5% de desconto
    if pagamento == "PIX":

        print(f"{entrada} - {pagamento} R$ {valor * 0.95}")

    # Débito: não muda o valor
    elif pagamento == "débito":

            print(f"{entrada} - {pagamento} R$ {valor}")

    # Crédito: da 5% de acréscimo
    elif pagamento == "crédito":

        print(f"{entrada} - {pagamento} R$ {valor * 1.05}")


            
        







