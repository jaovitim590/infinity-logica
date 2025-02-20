"""[LPIA-A03] Você está criando um programa em Python para simular um jogo simples de adivinhação. O programa deve ter um 
número fixo, por exemplo, 7, que o jogador deve adivinhar. O jogador terá até 3 tentativas para acertar o número.

Implemente o jogo utilizando um loop while para permitir que o jogador faça múltiplas tentativas até acertar ou atingir o 
limite de tentativas. Utilize a estrutura else para exibir uma mensagem de encorajamento caso o 
jogador acerte e uma mensagem de consolo caso as 3 tentativas se esgotem sem sucesso."""

num = 5
tentativas = 3

print("voce tera que adivinhar um numero entre 1 a 10!")

while  tentativas > 0 :
  chute = int(input("escreva seu chute:"))

  if chute == num:
    print(f"voce acertou o numero secreto com {tentativas} tentativas restantes!")
  else:
    tentativas -= 1
    if tentativas > 0:
      print(f"Erro! Você tem {tentativas} tentativas restantes.")
    else:
      print(f"Você perdeu! As tentativas acabaram. O número era {num}.")