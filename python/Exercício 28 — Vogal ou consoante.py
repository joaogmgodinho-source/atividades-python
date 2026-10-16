#  Exercício 28 — Vogal ou consoante
#  Aluno: João Gustavo
#  Objetivo: Leia uma letra minúscula e informe se ela é vogal ou consoante.

# Pede a letra
letra = input("Digite uma vogal ou uma consoante: ")

# Compara se ela é uma vogal ou uma consoante
if letra in "a" "e" "i" "o" "u":
    print("Essa letra é uma vogal")
else:
    print("Essa letra é uma consoante")