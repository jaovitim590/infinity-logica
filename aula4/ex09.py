"""Crie um programa que use um laço for para contar de 1 a 20. Use condicionais para
identificar números pares e ímpares. Pare o loop ao encontrar o número 15, usando break."""

for i in range(1,21):
  if i == 15:
    break
  elif i % 2 != 0 :
    print(f" {i} é numero impar!")
  else:
    print(f" {i} é numero par!")