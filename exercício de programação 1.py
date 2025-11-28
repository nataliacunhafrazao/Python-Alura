#Faça uma ficha cadastral para um paciente

def remover_espacos_a_esquerda(texto):
    return texto.lstrip()
nome = input("Informe seu nome:")
idade = int(input("Informe sua idade:"))
endereço = input("Infome seu endereço:")
telefone = input("Informe seu telefone:")
comorbidade = input("Possui alguma comorbidade?")

nome = remover_espacos_a_esquerda (nome)
endereço = remover_espacos_a_esquerda (endereço)
telefone = remover_espacos_a_esquerda (telefone)
comorbidade = remover_espacos_a_esquerda(comorbidade)

#exibição dos dados
print("Nome:",nome)
print("Endereço",endereço)
print("Telefone",telefone)
print("Possui alguma comorbidade?:",comorbidade)

# Lembrando que esta função só pode ser usada para valores com strings(Não aceita valores númericos)
#Próxima aula ver sobre a técnica de slice e posteriormente fazer as revisões de if,else ,while e formatação de strings