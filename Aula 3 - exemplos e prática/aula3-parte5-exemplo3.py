#ler três valores e calcular as raízes reais aplicando bhaskara
#ob.: math.sqrt só aceita valores positivos, então se delta for negativo ele não funciona

a = float(input("digite o valor de a: "))
b = float(input("digite o valor de b: "))
c = float(input("digite o valor de c: "))

if(a==0):
  print("a = 0. Erro de divisão.")
else:
  raizPositiva = (-b+(b**2-4*a*c)**0.5)/(2*a)
  raizNegativa = (-b-(b**2-4*a*c)**0.5)/(2*a)
  print("As raízes são: x1 =",raizPositiva,"e x2 =",raizNegativa)