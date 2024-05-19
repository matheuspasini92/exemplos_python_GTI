#programa que conta a quantidade de vogais presentes em uma string

palavra = input("Digite uma palavra ou frase: ")
vogais = "aeiouAEIOU"
qtd = 0

for letra in palavra:
  if(letra in vogais):
    qtd += 1

print(f"A quantidade de vogais em '{palavra}' é {qtd}")