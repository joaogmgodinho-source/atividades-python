/*
 Exercício 2 — Operações básicas
 Aluno: João Gustavo
 Objetivo: Leia dois números inteiros e mostre a soma, a subtração (primeiro menos o segundo) e a multiplicação entre eles
*/

programa {
  funcao inicio() {
    
    // Criando as variaveis dos numeros e soma, do tipo inteiro
    inteiro n1, n2, soma, mult, sub

    // Pede para digitar o primeiro número
    escreva("Digite o primeiro número: ")
    leia(n1)

    // Pede para digitar o segundo número
    escreva("Digite o segundo número: ")
    leia(n2)

    // Faz a soma, multiplicação e a subtração e guarda nas suas variaveis
    soma = n1 + n2
    mult = n1 * n2
    sub = n1 - n2

    // Mostra os resultados na tela
    escreva("As soma dos números é: ", soma, "\n")
    escreva("A multiplicação dos números é: ", mult, "\n")
    escreva("A subtração dos números é: ", sub, "\n")
  }
}
