/*
 Exercício 16 — Saque no caixa eletrônico
 Aluno: João Gustavo
 Objetivo: Leia o saldo da conta e o valor que a pessoa quer sacar. Se houver saldo suficiente, mostre o novo saldo.
Senão, mostre Saldo insuficiente.
*/

programa {
  funcao inicio() {
    
    // Cria as variaveis do saldo e saque do tipo inteiro
    inteiro saldo, saque

    // Pede o saldo disponivel
    escreva("Digite o seu saldo: ")
    leia(saldo)

    // Pede o quanto você quer sacar
    escreva("Digite o quanto você quer sacar: ")
    leia(saque)

    // compara se o saque é maior que o saldo, se sim, da erro e 
    se (saque > saldo) {
      escreva("Saldo insuficiente")
    } senao {
      saldo = saldo - saque
      escreva("saque realizado, novo saldo: ", saldo, "R$")
    }


  }
}
