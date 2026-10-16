#  Exercício 35 — Calculadora
#  Aluno: João Gustavo
#  Objetivo: Leia dois números e um operador (+, -, * ou /) e mostre o resultado da operação.
# • Na divisão, se o segundo número for zero, mostre Erro: divisão por zero.
# • Se o operador não for nenhum dos quatro, mostre Operador inválido.

# Pede o primeiro número 
n1 = int(input("Digite o primeiro número: "))

# Pede o segundo núemero 
n2 = int(input("Digite o segundo número: "))

# Pede para escolher o operador
op = input("Escolha o operador (+, -, * ou /): ")

# Faz todas as comparações com os operadores e mostra o resultado, ao não ser que de operador invalido
if op == "+":
    print(f"Soma: {n1 + n2}")
elif op == "-":
    print(f"Sub: {n1 - n2}")
elif op == "*":
    print(f"Multiplicação: {n1 * n2}")
elif op == "/":
    # Caso divisão seja escolhida, ele ve se o segundo número é igual a zero, se sim, ele da erro, se não, apenas continua
    if n2 == 0:
        print("Erro: divisão por zero")
    else:
        print(f"Divisão: {n1 / n2}")
else:
    print("Operador invalido")