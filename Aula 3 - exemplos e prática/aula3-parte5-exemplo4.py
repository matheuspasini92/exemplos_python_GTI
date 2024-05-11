#ler o saldo médio de uma conta, calcula e escreve o limitecfe tabela:
#
#Saldo médio                     |Limite
#menor que R$ 500,00             |não há limite
#de R$ 500,00 a R$ 1.000,00      |8% do saldo médio
#maior ou igual a R$ 1.000,00    |15% do saldo médio

saldo = float(input("Digite o saldo médio da sua conta, pode ser negativo: "))

if(saldo<500):
  print("Não há limite disponível.")
if(saldo>=500 and saldo<1000):
  print("Limite disponível de: R$",saldo*0.08)
if(saldo>=1000):
  print("Limite disponível de: R$",saldo*0.15)