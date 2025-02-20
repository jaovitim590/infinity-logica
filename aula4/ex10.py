"""Peça ao usuário para inserir 10 números. Use um laço for com condicionais para contar quantos
são positivos e quantos são negativos. Pare o loop se o número 0 for inserido, usando break."""

positivos = 0
negativos = 0

for i in range(10):
    while True:
        try:
            
            numero = float(input(f"Digite o {i+1}º numero: "))
            if numero > 0:
              positivos += 1
            else:
              negativos += 1
            break  
        except ValueError:
         
            print("Por favor, digite um número válido.")

    if numero == 0:
              break

print(positivos)
print(negativos)