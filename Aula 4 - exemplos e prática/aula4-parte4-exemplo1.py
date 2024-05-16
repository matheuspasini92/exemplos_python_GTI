#jogo pedra, papel e tesoura
import random

jogador = input("Escola a opção: pedra, papel ou tesoura = ")
comp = random.choice(["pedra","papel","tesoura"]) 

print("Computador escolheu: ",comp)
if (jogador==comp):
  print("Empate")
elif(jogador=="pedra"):
  if(comp=="tesoura"):
    print("Pedra quebra tesoura! Você venceu!")
  else:
    print("Papel cobre pedra... Você perdeu!")
elif(jogador=="papel"):
  if(comp=="pedra"):
    print("Papel cobre pedra! Você venceu!")
  else:
    print("Tesoura quebra pedra... Você perdeu!")
elif(comp=="papel"):
  print("Tesoura corta papel! Você venceu!")
else:
  print("Pedra quebra tesoura... Você perdeu!")