#Ler dois valores a e b naturais. Escrever e somar os valores ímpares existentes entre a e b

a = int(input("Digite o valor inicial do intervalo: "))
while(a<0):
  print("Valor inicial não pertence ao conjunto dos Naturais...")
  a = int(input("Digite novamente o valor inicial do intervalo: "))

b = int(input("Digite o valor final do intervalo: "))
while(b<0):
  print("Valor final não pertence ao conjunto dos Naturais...")
  b = int(input("Digite novamente o valor final do intervalo: "))

  if(a>b):
    aux = a
    a = b
    b = aux
  if(a%2==0):
    a = a + 1
  soma = 0
  print("Valores ímpares do intervalo:")
  while(a<=b):
    print(a)
    soma = soma + a
    a = a + 2
  print("Soma dos ímpares do intervalo: ",soma)