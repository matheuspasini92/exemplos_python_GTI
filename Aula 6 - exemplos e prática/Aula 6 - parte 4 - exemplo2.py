#implemente um programa que escreve os n primeiros números primos

quant = int(input("Informe a quantidade de números primos: "))
while(quant<=0):
  print("Valor inválido. A quantidade deve ser positiva e diferente de zero")
  quant = int(input("Informe novamente a quantidade de números primos: "))

num = 2
contPrimos = 0
while(contPrimos<quant):
  contaDivisores = 0
  d = 1
  while(d<=num):
    if(num%d==0):
      contaDivisores = contaDivisores + 1
    d = d + 1
  if(contaDivisores==2):
    print(num)
    contPrimos = contPrimos + 1
  num = num + 1