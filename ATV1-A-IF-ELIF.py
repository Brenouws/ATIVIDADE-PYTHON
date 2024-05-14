print ("Bem vindo a loja do Breninho") # Exigencia numero 1, ter uma mensagem de boas vindas com meu nome
preço = float(input("Entre com o preço do produto :")) # Exigencia numero 2 input do valor unitario 
quant = int(input("Entre com a quantidade do produto :")) #Exigencia numero 2 input da quantidade do produto 
precointeiro = preço * quant #calculando o preço inteiro fazendo o preço * quantidade

# Exigencia numero 5 Abaixo a estrutura de IFS-ELIFS-ELSE para calcular o desconto
if precointeiro >= 2500 and precointeiro < 6000: # estrutura de if, elif e else
    desconto = precointeiro * 4 / 100 # Exigencia numero 4, calculo do desconto de 4% (Nesse caso)
    print ("Boas compras, volte sempre a loja do Breninho") #Mensagem de obrigado e de despedidas
    print (f"Seu desconto foi de {desconto} R$ que legal :)") # Um bonus que fiz para mostrar qual o valor do desconto que a pessoa recebeu
    print ("O total de sua compra foi ", precointeiro - desconto,"R$")  #Exigencia numero 4, Valor total com desconto
    print (f"Sem o desconto você teria gasto {precointeiro:.2f} R$") # Exigencia numero 4, Valor total sem desconto
elif precointeiro < 10000 and precointeiro > 6000:
    desconto = precointeiro * 7 / 100 #Exigencia numero 4, calculo do desconto de 7% (Nesse caso)
    print ("Boas compras, volte sempre a loja do Breninho")
    print (f"Seu desconto foi de {desconto} R$ que legal :)")
    print ("O total de sua compra foi ", precointeiro - desconto,"R$")
    print (f"Sem o desconto você teria gasto {precointeiro:.2f} R$")
elif precointeiro >= 10000:
    desconto = precointeiro * 11 / 100 #Exigencia numero 4, calculo do desconto de 11% (Nesse caso)
    print ("Boas compras, volte sempre a loja do Breninho")
    print (f"Seu desconto foi de {desconto} R$ que legal :)")
    print ("O total de sua compra foi ", precointeiro - desconto,"R$")
    print (f"Sem o desconto você teria gasto {precointeiro:.2f} R$")
else :
    print ("Boas vindas a loja do Breninho")
    print("Infelizmente você não obteve nenhum desconto :/ ") #Sem desconto pq não adquiriu a quantidade suficiente
    print(f"O valor total de sua compra foi :{precointeiro:.2f}R$")
    
#Comentario extra apenas para dizer que sim, eu sei que ELSE fara com que qualquer opcão que não cumpra o requisito sera dada como sem desconto, porem fiz apenas o que pedia nas exigencias
#Também não comentei as estruturas de IFS pq são todas iguais mudando apenas o numero do calculo de desconto, o que facilitaria com uma função
