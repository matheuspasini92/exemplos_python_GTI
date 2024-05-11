#verifica se o num2 é o maior valor dos três

num1 = int(input("Digite o primeiro valor inteiro: "))
num2 = int(input("Digite o segundo valor inteiro: "))
num3 = int(input("Digite o terceiro valor inteiro: "))

if (num2>num1 and num2>num3):
  print("O valor",num2,"é o maior valor")


#verifica se o num2 e num3 são múltiplos

num1 = int(input("Digite o primeiro valor inteiro: "))
num2 = int(input("Digite o segundo valor inteiro: "))
num3 = int(input("Digite o terceiro valor inteiro: "))

if(num2%num3==0 or num3%num2==0):
  print(num2," e ",num3,"são múltiplos")

#verifica se os três valores são iguais

num1 = int(input("Digite o primeiro valor inteiro: "))
num2 = int(input("Digite o segundo valor inteiro: "))
num3 = int(input("Digite o terceiro valor inteiro: "))

if(num1==num2 and num2==num3):
  print("Os três valores são iguais")
  
print("=========================")
print("Valor 1: ",num1)
print("Valor 2: ",num2)
print("Valor 3: ",num3)