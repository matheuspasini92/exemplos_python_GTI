#Implementando um programa que calcula a soma de n primeiros termos da série a seguir:
#1+1/2+1/3+1/4+1/5+... (entendemos que o primeiro termo,1, é 1/1)

nTermos = int(input("Informe a quantidade de termos: "))

if(nTermos<=0):
  print("Número de termos inválido")
else:
  soma = 0
  cont = 1
  while(cont<=nTermos):
    soma = soma + 1/cont
    cont += 1
  print("Soma dos termos: ",soma)