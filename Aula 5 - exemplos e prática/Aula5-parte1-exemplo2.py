#exibindo uma tabela de resultados
#mostrar a tabela dos números de 1 a 50 e suas respectivas raízes quadradas
import math

for num in range(1,51):
  print(f"{num:6}: {math.sqrt(num):.3f}")