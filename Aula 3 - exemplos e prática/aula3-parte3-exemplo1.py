#ler o horário de início de um jogo, em horas e minutos, e o horário de fim de jogo, em horas e minutos.
#Sabendo que a duração máxima do jogo é de 24 horas, determinar o tempo de duração do jogo em horas e munitos.


inicio_hora = int(input("Digite a hora de início do jogo: "))
inicio_minuto = int(input("Digite o minuto de início do jogo: "))
fim_hora = int(input("Digite a hora de fim do jogo: "))
fim_minuto = int(input("Digite o minuto de fim do jogo: "))

inicio_hora = inicio_hora*60 + inicio_minuto
fim_hora = fim_hora*60 + fim_minuto

if(inicio_hora < fim_hora):
  duracao = fim_hora - inicio_hora
else:
  duracao = 24*60 - inicio_hora + fim_hora

print("Tempo de duração do jogo: ",duracao//60," horas e ",duracao%60," minutos")