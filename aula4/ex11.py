"""Escreva um programa que use um laço for para imprimir números de 1 a 30.
Use uma condicional para verificar se um número é múltiplo de 5 e outro
para verificar se é maior que 20 e interromper o loop com break."""


for i in range(1, 31):
  if i % 5 == 0:
    print(f"{i} é multiplo de 5!")
  elif i > 20:
    print(f"{i} é maior que 20!")
  else:
    print(i)
  