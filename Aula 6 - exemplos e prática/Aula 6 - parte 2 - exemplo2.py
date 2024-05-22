#Implementando um programa que calcula a soma de n primeiros termos da série a seguir:
#2+4/3+6/5+8/7+10+9... (entendemos que o primeiro termo,1, é 1/1)

nTermos = int(input("Informe a quantidade de termos: "))

if(nTermos<=0):
  print("Número de termos inválido")
else:
  soma = 0
  cont = 1
  numerador = 2
  denominador = 1
  while(cont<=nTermos):
    soma = soma + numerador/denominador
    cont += 1
    numerador += 2
    denominador += 2
  print("Soma dos termos: ",soma)