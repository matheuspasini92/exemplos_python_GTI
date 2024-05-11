#determina o preço de venda dos produtos de uma loja conforme o preço de custo
#desses produtos. Deve ler o preço e calcular o valor de venda, cfe tabela:
#---------------------------------------------------
#Preço unitário de custo        |Preço de venda
#---------------------------------------------------
#valor abaixo R$10,00           |lucro de 70%
#de R$10,00 a menos de R$30,00  |lucro de 50%
#de R$30,00 a menor de R$50,00  |lucro de 40%
#valor acima ou igual a R$50,00 |lucro de 30%
#---------------------------------------------------

custo = float(input("Digite o preço de custo de um produto: "))

if(custo<0):
  print("Valor inválido")
else:
  if(custo<10):
    venda = custo*1.7
  if(custo>=10 and custo<30):
    venda = custo*1.5
  if(custo>=30 and custo<50):
    venda = custo*1.4
  if(custo>=50):
    venda = custo*1.3
  print("O preço de venda é: R$",venda)