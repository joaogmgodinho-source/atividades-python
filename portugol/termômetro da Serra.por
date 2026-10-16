/*
 Exercício 22 — Termômetro da Serra
 Aluno: João Gustavo
 Objetivo: Leia a temperatura do dia em °C (pode ter casas decimais) e mostre a mensagem conforme a tabela.
*/

programa {
  funcao inicio() {
    
    real temperatura

    escreva("Digite a temperatura: ")
    leia(temperatura)

    se (temperatura < 0) {
      escreva("Abaixo de zero - risco de geada")
    } senao se (temperatura < 10) {
      escreva("")
    }

  }
}
