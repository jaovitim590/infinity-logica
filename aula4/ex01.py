"""Tabuada de um Número:
Faça um programa que solicite um número ao usuário e use
um laço for para exibir a tabuada desse número (de 1 a 10)."""

num = int(input("insira um numero: "))

for i in range(1, 11):
  print(f"{num} x {i} = {num * i}")