print("OLÁ MUNDO")
MSG = "OLÁ MUNDO"
######COLOQUEI A AULA 001 E 002 NESTE ARQUIVO##
print(MSG)


nome=input("Informe seu nome:")
print("OLÁ {} ".format(nome))

l = ['abc', ['a', 'b', 'c'], 'd', ['a', ['abc', 'd']]]

c = 0



for e in l:


 c+=len(e)



print( c )

import numpy  as np

b = np.array([[1,2,3,5]])

c = b.transpose()

print(b.dot(c),sum(b),sum(c))


#No L[-1::-2], o -1 representa que começara do ultimo valor, no caso o 30, o ::-2 serve para dizer que o número pulará em -2 em -2 (Em dois em dois da direita para a esquerda) até chegar ao final da lista. Dessa forma, começará no valor 30, pulando -2, chegará no valor 10, pulando -2 novamente, chegará no valor -10. Como não há como pular mais -2, a execução é encerrada. Dessa forma, com o comando print(L[-1::-2]) irá apresentar [30,10,-10]. Por esse motivo a alternativa correta é a Letra A.