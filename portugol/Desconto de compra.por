/*
 Exercício 15 — Desconto na compra
 Aluno: João Gustavo
 Objetivo: Uma loja dá 10% de desconto em compras a partir de R$ 100,00. Leia o valor da compra e mostre o valor
final a pagar
*/

programa {
  funcao inicio() {
    
    // Cria as variaveis dos valores do tipo real
    real valor, desconto, total

    // Pede para digitar o valor da compra
    escreva("Digite o valor da compra: ")
    leia(valor)

    // compara de o valor da compra é maior que 100, se sim, ele faz a conta para ter 10% do valor da compra e subtrai do total, se nao, continua o valor original
    se (valor > 100){
      desconto = valor * 0.10
      total = valor - desconto
    } senao {
      total = valor
    }

    // mostra o valor total a se pagar
    escreva("O valor a se pagar é: ", total)

  }
}
