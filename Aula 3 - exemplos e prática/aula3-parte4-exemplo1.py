#ler quatro valores e colocar em ordem crescente

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
num3 = int(input("Digite o terceiro valor: "))
num4 = int(input("Digite o quarto valor: "))

if (num2<num1):
  aux = num1
  num1 = num2
  num2 = aux 

if (num3<num1):
  aux = num1
  num1 = num3
  num3 = aux 

if (num4<num1):
  aux = num1
  num1 = num4
  num4 = aux 

if (num3<num2):
  aux = num2
  num2 = num3
  num3 = aux 

if (num4<num2):
  aux = num2
  num2 = num4
  num4 = aux 

if (num4<num3):
  aux = num3
  num3 = num4
  num4 = aux 

print("Ordem crescente: ",num1,num2,num3,num4)
print("Ordem decrescente: ",num4,num3,num2,num1)