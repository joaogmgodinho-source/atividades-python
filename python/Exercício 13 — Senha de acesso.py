# Exercício 13 — Senha de acesso
# Aluno: João Gustavo
# Objetivo: A senha correta do sistema é senai2026. Leia a senha digitada e mostre Acesso liberado se ela estiver
# correta ou Acesso negado se estiver errada.

# Pede para digitar a senha
senha = input("Digite a senha: ")

# Compara se a senha está correta, se sim, ele libera o acesso
if senha == "senai2026":
    print("Acesso liberado")
else:
    print("Acesso negado")
