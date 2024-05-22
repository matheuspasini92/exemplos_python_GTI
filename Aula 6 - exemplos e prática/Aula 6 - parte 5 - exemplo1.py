#fatorial dos 100 primeiros inteiros
fat = 1
for num in range(1,101):
  fat = fat * num

  print(fat)

#ou, fatorial dos 100 primeiros inteiros
fat = 1
cont = 1
while(cont<=100):
  fat = fat * cont
  cont = cont + 1 

print(fat)

#ou, fatorial dos 100 primeiros inteiros

numero = 0
while(numero<=99):
  fat = 1
  aux = 2
  while(aux<=numero):
    fat = fat * aux
    aux = aux + 1
  print(f"O fatorial de {numero} é igual á {fat}")
  numero = numero + 1