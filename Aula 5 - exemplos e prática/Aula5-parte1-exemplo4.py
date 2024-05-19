#algoritmo de Heron. Calcular a raiz quadrada, começando com um chute n, 
#se n*n é próximo de x, pare e considere que a resposta é n
#senão, o próximo chute será a media entre n e x/n
#usando esse novo valor, repita o processo a aprtir do passo 2 até conseguir um resultado suficientemente próximo

num = int(input("Valor desejado: "))
total = int(input("Quantidade de repetições: "))

aprox = 1
for cont in range(1,total+1):
  aprox = (aprox + num/aprox)/2
  print(f"{cont:3}: {aprox:.5f}")
  
print("------------")
print(f"Raiz aproximada: {aprox:.5f}")