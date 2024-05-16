#determinar as condições climáticas a partir de medições da temperatura e umidade atuais
#ler temperatura e umidade, imprimir a condição atual

temperatura = float(input("Digite a temperatura atual, em Celsius: "))
umidade = float(input("Digite a umidade relativa do ar local atual: "))

if (temperatura>30):
  if(umidade>60):
    print("Quente e umido")
  else:
    print("Quente")
elif (temperatura>20 and temperatura<=30):
  print("Ameno")
elif (temperatura>=10 and temperatura<20):
  print("Frio")
else:
  print("Muito frio")  