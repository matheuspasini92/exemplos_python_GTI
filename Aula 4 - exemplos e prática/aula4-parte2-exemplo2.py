#determina conceito de aluno em função da nota

nota = float(input("Digite a nota do aluno em decimal, ex.:10,20,30,... : "))


if(nota>=90):
  print("Conceito A")
else:
  if(nota>=80):
    print("Conceito B")
  else:
    if(nota>=70):
      print("Conceito C")
    else:
      if(nota>=60):
        print("Conceito D")
      else:
        print("Conceito F")