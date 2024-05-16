#calcular raizes de equação de segundo grau para delta positivo
import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = math.pow(b,2) - 4*a*c

if (a==0):
  print("Divisão por zero não existe. Valor de a: ",a)
elif (delta>=0):
  x1 = (-b + math.sqrt(delta))/(2*a)
  x2 = (-b - math.sqrt(delta))/(2*a)
  print("O valor das raízes reais são: x' = ",x1,", x'' =",x2)
else:
  print("Não existem raízes reais")