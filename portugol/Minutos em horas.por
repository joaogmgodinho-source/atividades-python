/*
 Exercício 5 — Minutos em horas
 Aluno: João Gustavo
 Objetivo: Leia uma quantidade de minutos (número inteiro) e mostre quantas horas e quantos minutos ela representa
*/

programa {
  funcao inicio() {
    
    // cria as variaveis do numero que vai ser convertido e das horas e minutos de tipo inteiro
    inteiro n1, horas, minutos

    // Pede para digita o numero para ser convertido
    escreva("Digite uma quantidade de minutos para tranformar me horas e quantos minutos representa: ")
    leia(n1)

    // faz a conta para as horas
    horas = n1 / 60

    // faz a conta para os minutos
    minutos = n1 % 60

    // mostra em forma de horas e minutos
    escreva(horas, " horas e ", minutos, " minutos")

  }
}
