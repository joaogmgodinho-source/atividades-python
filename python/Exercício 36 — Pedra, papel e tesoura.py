#  Exercício 36 — Pedra, papel e tesoura
#  Aluno: João Gustavo
#  Objetivo: Dois jogadores digitam suas jogadas: pedra, papel ou tesoura. Mostre quem venceu ou se deu empate.
# Regras: pedra vence tesoura, tesoura vence papel e papel vence pedra. Se algum jogador digitar uma opção
# que não existe, mostre Jogada inválida.

# Pede a jogada do jogador 1
jogador1 = input("Jogador 1: Faça sua jogada (pedra, papel ou tesoura): ")

# Pede a jogada do jogador 2
jogador2 = input("Jogador 2: Faça sua jogada (pedra, papel ou tesoura): ")

# Faz todas as comparações para o jogador 1 ganhar
if (jogador1 == "pedra" and jogador2 == "tesoura") or (jogador1 == "tesoura" and jogador2 == "papel") or (jogador1 == "papel" and jogador2 == "pedra"):
    print("Jogador 1 venceu!")
# Faz todas as compararações para o jogador 2 ganhar
elif (jogador2 == "pedra" and jogador1 == "tesoura") or (jogador2 == "tesoura" and jogador1 == "papel") or (jogador2 == "papel" and jogador1 == "pedra"):
    print("Jogador 2 venceu!")
# Compara se não é empate
elif jogador1 == jogador2:
    print("Empate!")
# Compara se a jogada dos 2 jogadores foi invalida
elif jogador1 != "pedra" "tesoura" "papel" or jogador2 != "pedra" "tesoura" "papel":
    print("Jogada invalida")