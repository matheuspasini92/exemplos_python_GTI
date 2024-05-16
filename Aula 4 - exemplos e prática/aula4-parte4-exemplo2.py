#conferencia de pressão arterial, cfe tabela internacional

sist = int(input("Sistólica: "))
diast = int(input("Diastólica: "))

if(diast>=120 or sist>=180):
  print("Crise hipertensiva")
elif((diast>=90 and diast<120) or (sist>=140 and sist<180)):
  print("Hipertensão estágio II")
elif((diast>=89 and diast<90) or (sist>=130 and sist<140)):
  print("Hipertensão estágio I")
elif(diast<80 and sist<130 and sist>=120):
    print("Elevada")
elif(diast<80 and sist<120):
  print("Normal")