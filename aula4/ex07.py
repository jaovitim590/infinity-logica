"""Crie um programa que solicite uma palavra ao usuário e use um laço for com
uma condicional para contar quantas vogais (a, e, i, o, u) a palavra contém."""

palavra = input("digite uma palavra: ")
numero_de_vogais = 0

for letra in palavra:
  if letra in ("a,e,i,o,u"):
    numero_de_vogais += 1

print(numero_de_vogais)