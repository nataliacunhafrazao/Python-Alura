#Nesta aula o professor ensinou sobre formatação de strings. Isto deixa o código mais legível#
print("INTERPOLAÇÃO DE STRINGS")    
print("tentativa {} de {}".format(3,10))

#Formatando números como moeda#
print("R${:f}".format(1.59))


#O 2f é para formatar até duas casas deciimais#
print("R${:.2f}".format(1.59))

#formatando datas#
print("Data {:02d} /" "{:02d}/" "{:04d}" .format(2,8,2023))

#praticando#
print("Olá Sr.{1} {0} ".format("Cordeiro","Leonardo"))
########################################colequei organizar o código
print("Olá Sr.(a){1} {0}".format("Junqueira","Marieta"))
#####################coloquei para organizar o código
print("A Data de hoje é {:02d}/""{:02d}/""{:04d}".format(16,5,2026))
##############
print("Sua compra deu o total de:R$ {:.2f}".format(152.50))
###################´#~#####################################
print("Meu salário é de R$ {:.4f}".format(1.860))

print("Olá {1} {0}".format("Frazão","Juliana"))
