"""Escreva um programa que solicite 5 notas de alunos. Use um laço for
para somar as notas e uma condicional para exibir a média e a
classificação ("Aprovado" para média >= 6,

"Reprovado" para média < 6)."""

notas = 0

for i in range(5):
    while True:
        try:
            
            numero = float(input(f"Digite a {i+1}º nota: "))
            notas += numero
            if numero >= 6:
              print("Aprovado")
            else:
              print("Reprovado")
            break  
        except ValueError:
         
            print("Por favor, digite um número válido.")

