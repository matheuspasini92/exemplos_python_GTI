#ler 10 valor float, representando alturas de pessoas, calcular e exibir a média das alturas
#mostrando a maior altura digitada

import random

total = 0

for cont in range(1,11): 
  altura = float(input(f"Digite a altura da {cont}º pessoa em metros: "))
  total = total + altura

media = total/10
print(f"A média das alturas é: {media:.3f}")

#ler 10 valor float, representando alturas de pessoas, calcular e exibir a média das alturas e a maior altura
import random
total = 0
maior = 0

for cont in range(1,11):
  altura = float(input(f"Digite a altura da {cont}º pessoa em metros: "))
  total = total + altura
  alt = random.uniform(1.50, 2.10)
  if (alt>maior):
    maior = alt

media = total/10
print(f"A média das alturas é: {media:.3f}")
print(f"A maior altura é {maior}")



#sortear 10 alturas, representando alturas de pessoas, calcular e exibir a média das alturas e a maior altura
import random
total = 0
maior = 0

for cont in range(1,11):
  alt = random.uniform(1.50, 2.10)
  total = total + alt
  if (alt>maior):
    maior = alt

media = total/10
print(f"A média das alturas é: {media:.2f}")
print(f"A maior altura é {maior}")