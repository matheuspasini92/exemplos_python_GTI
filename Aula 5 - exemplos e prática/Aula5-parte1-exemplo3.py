#somatório de 1 até num

num = int(input("Digite o valor final para a soma de todos os valores acumulados: "))
soma = 0

for cont in range(1,num+1):
  soma = soma + cont

print(f"A soma de 1 até {num} é {soma}")