/*
 Exercício 13 — Senha de acesso
 Aluno: João Gustavo
 Objetivo: A senha correta do sistema é senai2026. Leia a senha digitada e mostre Acesso liberado se ela estiver
correta ou Acesso negado se estiver errada.
*/

programa {
  funcao inicio() {
    
    // Cria a variavel da senha digitada de tipo cadeia
    cadeia senha

    // Pede para digitar a senha
    escreva("Digite a senha: ")
    leia(senha)

    // Compara se a senha digitada é igual a senha correta, se sim, acesso é liberado, se não, o acesso é negado
    se (senha == "senai2026"){
      escreva("Acesso liberado")
    } senao {
      escreva("Acesso negado")
    }

  }
}
