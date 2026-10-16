/*
 Exercício 9 — Par ou ímpar
 Aluno: João Gustavo
 Objetivo: Leia um número inteiro e informe se ele é par ou ímpar.
*/

programa {
  funcao inicio() {
    
    // Cria a variavel do numero de tipo inteiro
    inteiro n1

    // Pede para digitar o numero
    escreva("Digite um número: ")
    leia(n1)

    // compara se o resto da divisão do numero por 2 é igual a 0, se sim é par, se nao é impar
    se (n1 % 2 == 0) {
      escreva("esse número é par")
    } senao {
      escreva("esse número é impar")
    }

  }
}
