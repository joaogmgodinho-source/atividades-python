/*
 Exercício 8 — Positivo ou negativo
 Aluno: João Gustavo
 Objetivo: Leia um número inteiro e informe se ele é positivo ou negativo. Neste exercício, considere o zero como
positivo.
*/

programa {
  funcao inicio() {
    
    // Cria a variavel do numero de tipo inteiro
    inteiro n1

    // pede para digitar um numero positivo ou negativo
    escreva("Digite um número (positivo ou negativo): ")
    leia(n1)

    // compara se o numero digita é menor que 0, se sim, mostra que é negativo, se não, mostra que é positivo
    se (n1 < 0){
      escreva("esse número é negativo")
    } senao {
      escreva("esse número é positivo")
    }

  }
}
