/*
 Exercício 17 — Positivo, negativo ou zero
 Aluno: João Gustavo
 Objetivo: Leia um número e informe se ele é positivo, negativo ou zero.
*/

programa {
  funcao inicio() {
    
    // Cria uma variavel do número de tipo inteiro
    inteiro n1

    // Pede para digitar um número
    escreva("Digite um número: ")
    leia(n1)

    // compara se o número é maior que zero, igual a zero ou menor que zero, e mostra o resultado
    se (n1 > 0){
      escreva("O seu número é positivo")
    } senao se (n1 == 0) {
      escreva("O seu número é igual a zero")
    } senao {
      escreva("O seu número é negativo")
    }



  }
}
