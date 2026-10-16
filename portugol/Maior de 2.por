/*
 Exercício 11 — O maior de dois
 Aluno: João Gustavo
 Objetivo: Leia dois números diferentes e mostre qual deles é o maior.
*/

programa {
  funcao inicio() {
    
    // Cria as variaveis para os 2 numeros de tipo inteiro
    inteiro n1, n2

    // Pede para digitar o primeiro número
    escreva("Digite o primeiro número: ")
    leia(n1)

    // Pede para digitar o segundo número
    escreva("Digite o segundo número: ")
    leia(n2)

    // compara se o primero numero é maior que o segundo, e mostra qual o maior
    se (n1 > n2){
      escreva(n1, " é maior que ", n2)
    } senao {
      escreva(n2, " é maior que ", n1)
    }

  }
}
