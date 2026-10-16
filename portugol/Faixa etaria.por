/*
 Exercício 21 — Faixa etária
 Aluno: João Gustavo
 Objetivo: Leia a idade de uma pessoa e mostre a faixa etária conforme a tabela.
*/

programa {
  funcao inicio() {
    
    // Cria a variavel idade de tipo inteiro
    inteiro idade

    // Pede a idade
    escreva("Digite sua idade: ")
    leia(idade)

    // Faz todas as comparações para mostras a faixa etaria
    se (idade < 0){
      escreva("Idade inválida")
    } senao se (idade < 13){
      escreva("Criança")
    } senao se (idade < 18){
      escreva("Adolescente")
    } senao se (idade < 60){
      escreva("Adulto")
    } senao se (idade >= 60){
      escreva("Idoso")
    }

  }
}
