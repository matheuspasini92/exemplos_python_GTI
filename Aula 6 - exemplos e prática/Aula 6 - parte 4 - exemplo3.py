#A conjectura de goldbach diz que "todo número par maior ou igual a 4 é a soma de dois primos".
#Faça um programa que leia um valor n, inteiro e positivo, e escreva os n primeiros pares
#acima de 4 juntamente com os primos em que cada par pode ser decomposto
#Ex.:
#4 pode ser decomposto em 2 e 2
#6 pode ser decomposto em 3 e 3
#8 pode ser decomposto em 3 e 5
#10 pode ser decomposto em 5 e 5, ou 3 e 7
quant = int(input("Informe a quantidade de valores pares: "))
while(quant<=0):
  print("O valor deve ser positivo e maior que zero...")
  quant = int(input("Informe novamente a quantidade de valores pares: "))

num = 4  
pares = 1

while(pares<=quant):
  print("Numero: ",num)
  parte1 = num//2
  parte2 = parte1

  while(parte2<=parte1):
    contParte1 = 0
    d = 1
    while(d<=parte1):
      if(parte1 % d == 0):
        contParte1 = contParte1 + 1
      d = d + 1

    if(contParte1==2):
      d = 1
      contParte2 = 0
      while(d<=parte2):
        if(parte2%d==0):
          contParte2 = contParte2 + 1
        d = d + 1
      if(contParte2==2):
        print("Primo1: ",parte1," e Primo2: ",parte2)
        pares = pares + 1
        break

    parte1 = parte1 + 1
    parte2 = parte2 - 1
  num = num + 2
