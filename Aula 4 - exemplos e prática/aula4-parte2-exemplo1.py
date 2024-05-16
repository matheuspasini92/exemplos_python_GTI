#verifica se aluno é aprovado por média de notas, desde que tenha no mínimo 75% de frequencia

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
frequencia = float(input("Digite a frequência do aluno: "))

media = (nota1+nota2+nota3)/3

if(frequencia<75):
  print("Aluno reprovado por frequência baixa")
elif(media>=7 and media <=10):
  print("Aluno aprovado em G1, média = ",media)
elif(media<7 and media>4):
  print("Aluno necessita realizar exame G2")
  g2 = float(input("Digite a nota do G2: "))
  if(((media+g2)/2) >= 5 ):
    print("Aluno aprovado em G2, média = ",(media+g2)/2)
  else:
    print("Aluno reprovado em G2")
else:
  print("Aluno reprovado")