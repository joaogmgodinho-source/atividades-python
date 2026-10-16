/*
 Exercício 14 — Radar de velocidade
 Aluno: João Gustavo
 Objetivo: Numa via com limite de 80 km/h, leia a velocidade de um carro. Se ele passou do limite, mostre quantos
km/h acima ele estava. Senão, mostre Velocidade dentro do limite. Boa viagem!
*/

programa {
  funcao inicio() {
    
    // Cria a variavel do km de tipo inteiro
    inteiro km

    // pede a velocidade do carro
    escreva("Digite a velocidade do carro: ")
    leia(km)

    // Compara se o km passou do limite, se sim, ele ve quanto km foi passado e mostra, se nao, mostra que está dentro do limite
    se (km > 80) {
      escreva("Multado!, você passou ", km - 80, " km/h do limite")
    } senao {
      escreva("Velocidade dentro do limite. Boa viagem!")
    }

  }
}
