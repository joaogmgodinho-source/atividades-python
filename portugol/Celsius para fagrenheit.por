/*
 Exercício 4 — Celsius para Fahrenheit
 Aluno: João Gustavo
 Objetivo: Leia uma temperatura em graus Celsius e mostre o valor em Fahrenheit. Fórmula: F = C × 1.8 + 32.
*/

programa {
  funcao inicio() {

    // Cria as variaveis para os celsius e fahrenheit, de tipo inteiro
    inteiro celsius, fahrenheit

    // Pede para digitar os graus celsius
    escreva("Digite os graus em celsius para tranformar em fahrenheit: ")
    leia(celsius)

    // faz a formurla para ter os fahrenheit
    fahrenheit = celsius * 1.8 + 32

    // Mostra os gras em fahrenheit
    escreva(celsius, "° celsius é: ", fahrenheit, "° fahrenheit")

  }
}
