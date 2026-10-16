/*
 Exercício 20 — Dia da semana
 Aluno: João Gustavo
 Objetivo: Leia um número de 1 a 7 e mostre o dia da semana correspondente (1 = Domingo, 2 = Segunda-feira, … 7 =
Sábado). Para qualquer outro número, mostre Dia inválido.
*/

programa {
  funcao inicio() {
    
    // Cria a variavel do número e a do indice de tipo inteiro
    inteiro n1, i

    // Cria o vetor com todos os dias da semana de tipo cadeia
    cadeia dias[7] = {"Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado"}

    // Pede para digitar o numero para representar o dia
    escreva("Digite um número para representar um dia da semana (de 1 a 7): ")
    leia(n1)

    // Usa um "para" para percorrer o vetor e encontrar o dia
    para (i = 0;i < 7;i++){
      se (n1 == i+1){
        escreva(dias[i])
      }
    }


   
  }
}
