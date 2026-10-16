/*
 Exercício 3 — Média de três notas
 Aluno: João Gustavo
 Objetivo: Leia três notas (podem ter casas decimais) e mostre a média aritmética.
*/

programa {
  funcao inicio() {
    
    // Cria as variaveis para as 3 notas e o resultado de tipo real
    real n1, n2, n3, resultado

    // Pede pra digitar a primeira nota
    escreva("Digite a primeria nota: ")
    leia(n1)

    // Pede pra digitar a segunda nota
    escreva("Digite a segunda nota: ")
    leia(n2)

    // Pede pra digitar a terceira nota
    escreva("Digite a terceira nota: ")
    leia(n3)
  
    // Faz a conta da soma e da divisão para a média
    resultado = (n1 + n2 + n3) / 3.0

    // Mostra o resultado
    escreva("A sua média é: ", resultado)


  }
}
