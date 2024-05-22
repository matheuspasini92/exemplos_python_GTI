#Chico tem 1.50 metro e cresce 2 cm por ano, enquanto Zé 1.10 metro e cresce 3 cm por ano.
#Construir um programa que calcula e exibe qauntos anos serão necessários para que Zé seja maior que Chico.

altChico = 150
altZe = 110
anos = 0

while(altZe <= altChico):
  altChico = altChico + 2
  altZe = altZe + 3
  anos = anos + 1

print("Anos: ",anos)