#cálculo de salário liquido, lê salário bruto e total de dependentes
#retorna desconto de inss, IRRF, salário líquido
#base de cálculo de ir: bruto-inss-189,59 por dependente 
#ex.: 8000-828,39-189,59=6982,02
#ir será 1920,02 (27,5% de 6982,02)-869,36(parcela a deduzir na faixa de 27,5%) = R$1050,69

bruto = float(input("Digite o salário bruto: "))
dep = int(input("Digite a quantidade de dependentes: "))

if (bruto<1212):
  alinss = 0.075
  parcinss = 0
elif (bruto<= 2427.35):
    alinss = 0.09
    parcinss = 18.18
elif (bruto<= 3461.03):
    alinss = 0.12
    parcinss = 91
else:
    alinss = 0.14
    parcinss = 163.82  

inss = bruto*alinss-parcinss

if (inss>829.39):
  inss = 828.39

base = bruto-inss-189.59*dep

if(base<=1903.98):
  aliqirrf = 0
  parcirrf = 0
elif(base<=2826.65):
  aliqirrf = 0.075
  parcirrf = 142.8
elif(base<=3751.05):
  aliqirrf = 0.15
  parcirrf = 354.8
elif(base<=4664.68):
  aliqirrf = 0.225
  parcirrf = 636.13
else:
  aliqirrf = 0.275
  parcirrf = 869.36

irrf = base*aliqirrf-parcirrf

liquido = bruto - inss - irrf

print("Salário líquido de: R$ ",liquido)