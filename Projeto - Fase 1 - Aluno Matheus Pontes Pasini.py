#Implemente um programa que leia, valide e analise dados informados pelo usuário. Os dados são meteorológicos e
#referem-se aos dados de 2021 (de janeiro a dezembro) registrados em uma cidade.
#Toda entrada de dados deve ser validada. No caso de valor inválido, informe ao usuário o erro e permita que ele redigite o dado.
#Seu programa deve coletar os seguintes dados:
#• Mês: use valor numérico de 1 a 12 (janeiro a dezembro) para se referir aos meses do ano.
#Para cada mês do ano, informe:
#• Temperatura máxima do mês: devem estar em Celsius, garanta que estejam dentro de um intervalo válido para temperaturas, tal como: -60 graus à +50 graus.
#A seguir, seu programa deve calcular e exibir:
#• Temperatura média máxima anual: exibe a média das temperaturas máximas informadas.
#• Quantidade de meses escaldantes: quantidade de meses com temperaturas máximas acima de 33 graus Celsius.
#• Mês mais escaldante do ano: mês que registrou a maior temperatura máxima dentre todos os informados.
#O mês deve ser escrito na tela por extenso (janeiro a dezembro).
#• Mês menos quente do ano: mês que registrou a menor temperatura máxima dentre todos os informados.
#O mês deve ser escrito na tela por extenso (janeiro a dezembro).

#declaração das variáveis a serem utilizadas
escaldante = 0
maiorTemperatura = 0
menorTemperatura = 0
mediaMaximaMes = 0
maiorTemperatura = -float('inf') 
menorTemperatura = float('inf')
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

#laço de repetição for para iterar um intervalo de 1 até 12
for mes in range(1,13):

  #entrada de dado do usuário, informando a temperatura para o mês identificado pelo número
  print(f"Digite a temperatura do mes {mes}: ")
  tempMes = float(input())

  #laço de repetição while para garantia de entrada de valor de temperatura aceita
  #entre -60°C à +50°C. Permitindo nova entrada e atribuição no mês referido
  while(tempMes<-60 or tempMes>50):
    print(f"Temperatura inválida. Digite novamente uma nova temperatura para o mês {mes}")
    tempMes = float(input())

  #condição com variável contadora, para contar a quantidade de meses escaldantes (temperatura acima de 33° C)
  if(tempMes>33):
    escaldante += 1

   #verificar o mês mais quente e o identifica
  if(tempMes>maiorTemperatura):
    maiorTemperatura = tempMes
    mesMaisQuente = mes

  #verificar o mês menos quente e o identifica
  if(tempMes<menorTemperatura):
    menorTemperatura = tempMes
    mesMaisFrio = mes
    
  #variável acumuladora para somar as temperaturas máximas de cada mês, informadas pelo usuário
  mediaMaximaMes = mediaMaximaMes + tempMes

####### saindo do escopo do laço de repetição for #######

#cálculo da média máxima anual
mediaMaximaAnual = mediaMaximaMes / 12
print("-"*40)
#dados de retorno (saída) para o usuário
print(f"A média máxima anual, em 2021, foi de: {mediaMaximaAnual:.2f}°C")
print(f"A quantidade de meses escaldantes, temperatura acima de 33°C, foi de: {escaldante}")
print(f"A maior temperatura do ano, em 2021, foi de {maiorTemperatura}°C no mês de {meses[mesMaisQuente-1]}")
print(f"A menor temperatura do ano de 2021 foi de {menorTemperatura}°C no mês de {meses[mesMaisFrio-1]}")