"""[LPIA-A02] Crie um programa em Python para verificar se um número é positivo, negativo ou zero.
 O programa deve solicitar ao usuário que insira um número e, em seguida, imprimir uma mensagem indicando a natureza do número.

Se o número for maior que zero, exiba a mensagem "O número é positivo." Se for menor que zero, exiba 
"O número é negativo." Caso seja zero, a mensagem deve ser "O número é zero."

Utilize estruturas condicionais e formatação com F-string para criar o programa de forma clara."""

num = (input("insira um numero: "))

if float(num) > 0 :
  print("seu numero é positivo")
elif float(num) == 0 :
  print("seu numero é zero")
else:
  print("seu numero é negativo")