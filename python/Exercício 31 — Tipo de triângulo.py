#  Exercício 31 — Tipo de triângulo
#  Aluno: João Gustavo
#  Objetivo: Leia os três lados de um triângulo. Primeiro verifique se eles formam um triângulo: cada lado precisa ser
# menor que a soma dos outros dois. Se não formarem, mostre Esses lados não formam um
# triângulo. Se formarem, classifique:
# • Equilátero: os três lados iguais
# • Isósceles: exatamente dois lados iguais
# • Escaleno: os três lados diferentes

# Pede o primeiro lado
lado1 = int(input("Digite o primeiro lado: "))

# Pede o segundo lado
lado2 = int(input("Digite o segundo lado: "))

# Pede o terceiro lado
lado3 = int(input("Digite o terceiro lado: "))

# primero compara se ele é mesmo um triangulo, vendo se cada lado é
# menor que a soma dos outros dois
if lado1 >= lado2 + lado3 or lado2 >= lado1 + lado3 or lado3 >= lado2 + lado1:
    print("Esses lados não formam um triângulo")
# segundo compara se ele é equilatero, vendo se todos os lados são iguais
elif lado1 == lado2 and lado1 == lado3:
    print("Equilátero")
# Terceiro compara se ele é isóceles, vendo se tem exatamente dois lados iguais
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Isóceles")
# Se ele não encaixa em nenhuma das condições acima, é escaleno
else:
    print("Escaleno")