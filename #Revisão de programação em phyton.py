#Revisão de programação em phyton

nome=input("Digite seu nome:")
idade=int(input("Digite sua idade:"))
print(nome,"Tente adivinhar o número da sorte")
n1=int(input("Digite um número de 0 a 200:"))


numero_da_sorte=200

if n1 == numero_da_sorte:
    print("Parabéns este é o número da sorte")

else:
    print("Tente novamente,este não é o número correto")