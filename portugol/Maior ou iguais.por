/*
 Exercício 18 — Maior ou iguais
 Aluno: João Gustavo
 Objetivo: Leia um número e informe se ele é positivo, negativo ou zero.
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

    // compara se o primero numero é maior que o segundo, e mostra qual o maior, mas se os 2 forem iguais, mostra que os dois são iguais
    se (n1 > n2){
      escreva(n1, " é maior que ", n2)
    } senao se (n1 == n2){
      escreva("Os numeros são iguais")
    } senao {
      escreva(n2, " é maior que ", n1)
    }



  }
}
