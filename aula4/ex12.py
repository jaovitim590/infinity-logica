"""Peça ao usuário para inserir 5 preços de produtos. Use um laço for para
calcular o total. Aplique um desconto de 10% se o total ultrapassar 100 e
interrompa o loop com break."""

total = 0

for i in range(5):
    while True:
        try:
            
            numero = float(input(f"Digite o {i+1}º preco: "))
            total += numero
            break  
        except ValueError:
         
            print("Por favor, digite um número válido.")
if total > 100:
  total = total * 0.90
  print(f"o total fica: {total}")
else:
  print(f"o total fica: {total}")