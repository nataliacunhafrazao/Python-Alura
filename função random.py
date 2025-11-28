#Importar a função antes de usar o random
#gera números aleátorios
import random


#Atrubuir a váriavel numero random e depois utilizou a função
numero_random = random.random() *100
#conversão para um número inteiro
int(random.random() *100)
#print para aparecer o resultado
print(numero_random)

#round tem uma função semelhante ao random,contudo não precisamos inoortar a função.
print = round (numero_random)