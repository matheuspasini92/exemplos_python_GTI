#expressões longas, exercício para lógica
import math

a = float(input("Digite um valor para a: "))
b = float(input("Digite um valor para b: "))

funcao1  = ((math.sqrt(((a+3*b)/(b+1)))+math.pow(b,5))/math.fabs(b-a))+((math.sqrt(math.sqrt(a)+1))/(b+3*a+b+math.pow(a,5)))-1

print(funcao1)

funcao2 = (6*a*math.pow(b,a+1))-(((a+3*b)/(a+b-1))/(math.fabs(2*b-math.pow(a,3)-1)))

print(funcao2)

#exemplo simples de sobreposição de valores

val = 7
val = 9//4
val = val*1
val = val+10
val = 4+val-5*2
val = val//2
val = math.fabs(val-19)+2

print(val)
