a=input("Digite algo:")
print(f"o valor dessa variável é:",{type(a)})
print(f"só tem espaços?",a.isspace())
print(F"É NÚMERICO?",a.isnumeric())
print(f"Tem letras e números?",a.isalnum())
#######Todos os is:
#alfabetico - isalpha 
#numerico - isnumeric
#só tem espaços - isspace
#alfabético e numérico - isalnum
#está em maiúsculas - isupper
#está em minúculas - islower
#está só com a primeira letra em maiúsulas - istitle
#a variável A é um objeto que recebe os os paramêtros