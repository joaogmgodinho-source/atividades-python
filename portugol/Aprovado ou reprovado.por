/*
 Exercício 10 — Aprovado ou reprovado
 Aluno: João Gustavo
 Objetivo: leia duas notas de um aluno e calcule a média. Mostre a média e a mensagem Aprovado se ela for maior ou
igual a 7.0, ou Reprovado caso contrário.
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
    // compara de a media é maior ou igual a sete, se sim esta Aprovado, se nao, está reprovado
    se (media >= 7.0){
      escreva("Aprovado")
    } senao {
      escreva("Reprovado")
    }

  }
}
