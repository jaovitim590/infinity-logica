"""Crie um programa que use um laço for para somar
todos os números de 1 a 100 e exiba o resultado."""

soma = 0

for i in range(1, 101):
  soma = i + soma

print(f"a soma dos numeros de 1 a 100 é {soma}")