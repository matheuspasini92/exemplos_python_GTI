#Programa que leia um valor e verifica se é "perfeito". Naturais sem o zero
#Para ser perfeito, ele deve corresponder a soma dos seus divisores próprios
#Ex.: 6, pois 1+2+3 é 6

num = int(input("Informe um valor inteiro e positivo: "))
while(num<=0):
  print("Erro, o valor deve ser positivo")
  num = int(input("Informe novamente um valor inteiro e positivo: "))
soma = 0
d=1
while(d<=num/2):
  if (num%d==0):
    soma = soma + d
  d = d + 1

if(soma==num):
  print("Número perfeito!")
else:
  print("Número não é perfeito...")