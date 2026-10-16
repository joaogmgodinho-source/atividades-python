/*
 Exercício 6 — Compra na cantina
 Aluno: João Gustavo
 Objetivo: Leia o preço de um lanche, a quantidade comprada e o valor que o cliente pagou. Mostre o total da compra e
o troco. Considere que o valor pago é sempre suficiente.
*/

programa {
  funcao inicio() {
    
    // cria a variavel da quantidade de tipo inteira
    inteiro quantidade
    // Cria as variaveis do preco, valores, e troco de tipo real
    real preco, valor_total, valor_pago, troco

    // Pede o valor do lanche
    escreva("Digite o preço do lanche: ")
    leia(preco)

    // pede a quantidade que o cliente comprou
    escreva("Digite a quantidade que o cliente comprou: ")
    leia(quantidade)

    // Pede o quanto o cliente pagou
    escreva("Digite o quanto o cliente pagou: ")
    leia(valor_pago)

    // calcula o valor total
    valor_total = preco * quantidade

    // calcula o troco
    troco = valor_pago - valor_total

    // Mostra o valor total e o troco a se devolver
    escreva("O total da compra deu: ", valor_total, "\n")
    escreva("Deve ser devolvido ", troco, " de troco")



  }
}
