#usando break em um exemplo simples

for cont in range(20):  
  if cont > 10:
    break
  print(cont)

print("Continuação do programa")

#usando o continue exemplo simples

for cont in range(20):
  if cont%2==1:
    continue
  print(cont)

print("Continuação do programa")