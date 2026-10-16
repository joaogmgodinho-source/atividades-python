/*
 Exercício 12 — Divisão segura
 Aluno: João Gustavo
 Objetivo: Leia dois números: o dividendo e o divisor. Se o divisor for zero, mostre Erro: não existe divisão
por zero. Caso contrário, mostre o resultado da divisão.
*/

programa {
  funcao inicio() {
    
    // Cria as variaveis da divisão de tipo inteiro
    inteiro dividendo, divisor, resultado

    // pede para digitar o dividendo
    escreva("Digite um número: ")
    leia(dividendo)

    // Pede para digitar o divisor
    escreva("Digite um número para dividir: ")
    leia(divisor)

    // Compara se o divisor é igual a 0, se sim, mostra que deu erro, se não, faz o resultado e mostra ele
    se (divisor == 0){
      escreva("Erro: O divisor não pode ser igual a 0")
    } senao {
      resultado = dividendo / divisor
      escreva("O resultado da divisão é: ", resultado)
    }


  }
}
