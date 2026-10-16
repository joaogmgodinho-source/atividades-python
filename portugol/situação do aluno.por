/*
 Exercício 19 — Situação do aluno
 Aluno: João Gustavo
 Objetivo: Leia duas notas, calcule a média e mostre a situação do aluno conforme a tabela.
*/

programa {
  funcao inicio() {

    // Cria as variaveis para as 2 notas e a media de tipo real
    real n1, n2, media

    // Pede pra digitar a primeira nota
    escreva("Digite a primeria nota: ")
    leia(n1)

    // Pede pra digitar a segunda nota
    escreva("Digite a segunda nota: ")
    leia(n2)

    // Faz a conta da soma e da divisão para a média
    media = (n1 + n2) / 2.0

    // Mostra o resultado da media
    escreva("A sua média é: ", media, "\n")
    escreva("Situação:")
    // compara de a media é maior ou igual a sete, se sim esta Aprovado, se nao, está reprovado, tambem compara se é maior ou igual a 5, está de Recuperação
    se (media >= 7.0){
      escreva(" Aprovado")
    } senao se (media >= 5.0){
      escreva(" Recuperação")
    } senao {
      escreva(" Reprovado")
    }

  }
}
