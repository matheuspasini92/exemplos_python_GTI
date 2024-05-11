#ler 3 notas e fazer a média ponderada, considerando os pesos 5, 2.5 e 2.5.
#A maior nota deve ter peso 5

nota1 = float(input("Digite o valor da primeira nota: "))
nota2 = float(input("Digite o valor da segunda nota: "))
nota3 = float(input("Digite o valor da terceira nota: "))

if(nota1<0 or nota2<0 or nota3<0 or nota1>10 or nota2>10 or nota3>10):
  print("Erro. Alguma nota não está correta...")
else:
  if(nota1>nota2 and nota1>nota3):
    media = (nota1*5+nota2*2.5+nota3*2.5)/10
    print("A média das notas é: ",media)
  if(nota2>nota1 and nota2>nota3):
    media = (nota2*5+nota1*2.5+nota3*2.5)/10
    print("A média das notas é: ",media)
  if(nota3>nota1 and nota3>nota2):
    media = (nota3*5+nota1*2.5+nota2*2.5)/10
    print("A média das notas é: ",media)
    
#OUTRA FORMA ler 3 notas e fazer a média ponderada, considerando os pesos 5, 2.5 e 2.5.
#A maior nota deve ter peso 5

nota1 = float(input("Digite o valor da primeira nota: "))
nota2 = float(input("Digite o valor da segunda nota: "))
nota3 = float(input("Digite o valor da terceira nota: "))

if(nota1<0 or nota2<0 or nota3<0 or nota1>10 or nota2>10 or nota3>10):
  print("Erro. Alguma nota não está correta...")
else:
  maior = nota1
  if(maior<nota2):
    maior = nota2
  if(maior<nota3):
    maior = nota3
media = maior*0.5+(nota1+nota2+nota3-maior)*0.25
print("A média ponderada das notas é: ",media)