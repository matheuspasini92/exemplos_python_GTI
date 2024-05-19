#verificar se uma string é um palindromo

palavra = input("Digite uma palavra: ")

if(palavra == palavra[::-1]): 
  print(f"A palavra {palavra} é palíndromo")  
else:
  print(f"A palavra {palavra} não é palindromo")

print("-"*20)

#um jeito mais dificultoso de fazer, feito pelo professor, pra palíndromo

palavra = input("Digite uma palavra: ")

dif = False
for posicao in range(len(palavra)//2):
  if palavra[posicao] != palavra[-1-posicao]:
    dif = True
    break

if dif:
  print("A palavra não é palíndromo")
else:
  print("A palavra é palíndromo")