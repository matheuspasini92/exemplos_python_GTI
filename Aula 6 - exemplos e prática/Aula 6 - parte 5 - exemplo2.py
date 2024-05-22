#Programa que leia uma quantidade desconhecida de números. A seguir,
#o programa deve contar e escrever a qtd de valores pertencentes aos seguintes intervalos:
#[0,25],[26,50],[51,75],[76,100]
#A entrada de dados deve terminar quando for lido um valor negativo
#Ao final, o programa deve exibir ainda a quantidade de valores lidos

num = 0
soma = 0
cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
while(num>=0):
  num = int(input("Digite um número positivo ou digite um número negativo para sair:"))

  if(num>=0 and num<=25):
    cont1 = cont1 + 1
  if(num>=26 and num<=50):
    cont2 = cont2 + 1
  if(num>=51 and num<=75):
    cont3 = cont3 + 1
  if(num>=76 and num<=100):
    cont4 = cont4 + 1

  if(num>=0):
    soma = soma + 1

print(f"A quantidade de valores no intervalo de [0,25] é de {cont1}")
print(f"A quantidade de valores no intervalo de [26,50] é de {cont2}")
print(f"A quantidade de valores no intervalo de [51,75] é de {cont3}")
print(f"A quantidade de valores no intervalo de [76,100] é de {cont4}")
print(f"A quantidade de valores lidos foi de {soma}")