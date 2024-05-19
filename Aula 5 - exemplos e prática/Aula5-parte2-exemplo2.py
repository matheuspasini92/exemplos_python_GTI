#ler 10 valor float, representando alturas de pessoas, calcular e exibir a média das alturas

total = 0

for cont in range(1,11): 
  altura = float(input(f"Digite a altura da {cont}º pessoa em metros: "))
  total = total + altura

media = total/10
print(f"A média das alturas é: {media:.3f}")