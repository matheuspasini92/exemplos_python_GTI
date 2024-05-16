#reescrecendo usando elif

nota = float(input("Digite a nota do aluno em decimal, ex.:10,20,30,... : "))


if (nota>=90):
  print("Conceito A")
elif (nota>=80):
  print("Conceito B")
elif (nota>=70):
  print("Conceito C")
elif (nota>=60):
  print("Conceito D")
else:
  print("Conceito F")