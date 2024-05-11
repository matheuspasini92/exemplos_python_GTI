#ler um número inteiro de 4 digitos (garantindo isso). Verificar se o número
#é capicua quando, ou seja, quando lido da esquerda para a direita ou da 
#direita para a esquerda representa sempre o mesmo valor.

numero = int(input("Digite um inteiro de 4 digitos: "))

if(numero<1000 or numero>9999):
  print("Número inválido")
else:
  num1 = numero//1000
  resto = numero%1000
  num2 = resto//100
  resto = resto%100
  num3 = resto//10
  resto = resto%10
  num4 = resto
  if(num1==num4 and num2==num3):
    print("Numero é capicua")
  else:
    print("Numero não é capicua")