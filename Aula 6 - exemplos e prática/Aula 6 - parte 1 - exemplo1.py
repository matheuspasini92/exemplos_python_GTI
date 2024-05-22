#Programa que leia um valor inteiro e que verifica se o valor lido é primo. 
#Números primos possuem apenas 2 divisores, 1 e o próprio valor

num = int(input("Digite um valor inteiro para verificar se é primo ou não: "))

cont = 0 #contar os divisores, pois ele só pode ter dois divisores
d = 1

while (d <= num):
  if(num % d == 0):
    cont += 1
  d += 1

#só pode ter dois divisores, por isso que se usa o cont, pra verificar se existe somente dois divisores para o numero verificado
if cont == 2: 
  print(num, "é primo")
else:
  print(num,"não é primo")