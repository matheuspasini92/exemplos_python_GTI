# implementar o Jogo da Adivinhação, onde o objetivo é advinhar um numero sorteado pelo computador

import random

sorteado = random.randint(1,100)
#print(f"Sorteado: {sorteado}")

acertou = False

for tent in range(1,11):
  print(f"Tentativa {tent}: ", end="")
  num = int(input())
  if(num < sorteado):
    print("Tente um número maior...")
  elif (num > sorteado):
    print("Tente um número menor...")
  else:
    acertou = True
    break
 #nesse ponto, se acertou == True -> jogador ganhou
if acertou:   
  print("Você acertou!")
else:
  print(f"Você perdeu... O número era {sorteado}")