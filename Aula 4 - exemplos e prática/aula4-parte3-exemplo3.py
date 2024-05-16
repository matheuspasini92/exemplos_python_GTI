#calcular imc - genérico

peso = float(input("Digite o peso, em kg: "))
altura = float(input("Digite o peso, em metros: "))

imc = peso/(altura**2)

if(imc<18.6):
  print("Abaixo do peso")
elif(imc<25):
  print("Peso ideal")
elif(imc<30):
  print("Sobrepeso")
elif(imc<35):
  print("Obesidade grau I")
elif(imc<40):
  print("Obesidade grau II")
else:
  print("Obesidade grau III - mórbida")