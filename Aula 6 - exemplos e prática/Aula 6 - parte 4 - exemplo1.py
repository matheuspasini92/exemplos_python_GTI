#implemente um programa que escreve os divisores dos 100 primeiros valores inteiros

for num in range(1,101):
  print("="*20)
  print(">>Número: ",num)  
  d = 1
  while(d<=num):
    if(num%d==0):
      print(d," divide ",num)
    d = d+1