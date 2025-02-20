"""Contagem de Números Positivos e Negativos:
Escreva um programa que solicite ao usuário 10 números e use um
laço for com uma condicional para contar quantos são positivos e
quantos são negativos."""

numeros = []

for i in range(10):
    while True:
        try:
            
            numero = float(input(f"Digite o {i+1}º número: "))
            numeros.append(numero)
            break  
        except ValueError:
         
            print("Por favor, digite um número válido.")

for numero  in numeros:
  if numero < 0:
    print(f"{numero} é negativo!")
  else:
    print(f"{numero} é positivo!")