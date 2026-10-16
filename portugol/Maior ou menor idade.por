/*
 Exercício 7 — Maior ou menor de idade
 Aluno: João Gustavo
 Objetivo: Leia a idade de uma pessoa e informe se ela é maior de idade (18 anos ou mais) ou menor de idade
*/

programa {
  funcao inicio() {
    
    // Cria a variavel da idade de tipo inteira
    inteiro idade

    // Pede a idade 
    escreva("Digite sua idade: ")
    leia(idade)

    // Compara se a idade é maior de 18 se sim, mostra que é maior de idade, se não mostra que é menor de idade
    se (idade >= 18){
      escreva("Você é maior de idade")
    } senao {
      escreva("Você é menor de idade")
    }

  }
}
