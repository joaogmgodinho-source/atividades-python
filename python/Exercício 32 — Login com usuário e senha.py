#  Exercício 32 — Login com usuário e senha
#  Aluno: João Gustavo
#  Objetivo: O usuário cadastrado é aluno e a senha é 1234. Leia o usuário e a senha (os dois como texto) e mostre:
# • Usuário não encontrado, se o usuário estiver errado;
# • Senha incorreta, se o usuário estiver certo mas a senha estiver errada;
# • Login realizado com sucesso!, se os dois estiverem certos

# Pede para digitar o usuário
usuario = input("Digite o usuário: ")

# Pede para digitar a senha
senha = input("Digite a senha: ")

# Compara se a senha e o usuario estão certos
if (usuario == "aluno") and (senha == "1234"):
    print("Login realizado com sucesso!")
# Compara se a senha ta certa e o usuario errado
elif (usuario != "aluno") and (senha == "1234"):
    print("Usuário não encontrado")
# Compara se a senha ta errada e o usuario certo
elif (usuario == "aluno") and (senha != "1234"):
    print("Senha incorreta")  


