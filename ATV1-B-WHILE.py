
print ("Boas vindas a loja de sorvetes do breninho")      #Mensagem de boas vindas a minha loja (Exigencia 01 / 08)
print ("---------Cardapio-----------")
print ("---|Tamanho | Cupuaçu [CP] |Açai [AC]|---")
print ("---|   P    |   R$ 9.00    | R$ 11.00|---")
print ("---|   M    |   R$ 14.00   | R$ 16.00|---")
print ("---|   G    |   R$ 18.00   | R$ 20.00|---")
preco = 0  #Acumulador para somar os valores dos pedidos (Exigencia 05 / 08)
while True:  #Estrutura while com break e continue (Exigencia 07 / 08)
    sabor = input("Qual o sabor você ira querer ? (CP)(AC) : ") .upper() # Input perguntando qual sabor o cliente deseja (Exigencia 02 / 08)
    while sabor not in[ "CP", "AC" ]: #Loop caso o cliente erre o sabor (Exigencia 02 / 08)
        print ("Sabor inválido, tente novamente\n")                    
        sabor = input("Qual o sabor você ira querer ? (CP)(AC) : ") .upper()
    
    tamanho = input("E qual tamanho você deseja ? (P)(M)(G) : ") .upper()  #Input do tamanho juntamente com o loop (Exigencia 03 / 08)
    while tamanho not in ["P","M" ,"G"]:
        tamanho = input ("Tamanho invalido, tente novamente\n\nE qual tamanho você deseja ? (P)(M)(G)") .upper()               ##Estrutura de repetição para tamanho invalido
    # Logo abaixo estrutura com ifs e elifs (Exigencia 04 / 08)
    if sabor == "CP" and tamanho == "P":
        print ("Você pediu um cupuaçu no tamanho P: R$ 9.00\n")     #Tamanho P cupuacu 
        preco += 9    #Acumulando o valor na variavel
    elif sabor == "CP" and tamanho == "M":
        print ("Você pediu um cupuaçu no tamanho M: R$ 14.00\n")   #Tamanho M cupuacu 
        preco += 14  #Acumulando o valor na variavel
    elif sabor == "CP" and tamanho == "G": 
        print ("Você pediu um cupuaçu no tamanho G: R$ 18.00\n")    #Tamanho G cupuacu   
        preco += 18 #Acumulando o valor na variavel
    elif sabor == "AC" and tamanho == "P":
        print ("Você pediu um açai no tamanho P: R$ 11.00\n")      #Tamanho P Açai
        preco += 11 #Acumulando o valor na variavel
    elif sabor == "AC" and tamanho == "M":
        print ("Você pediu um açai no tamanho M: R$ 16.00\n")      #Tamanho M Açai
        preco += 16 #Acumulando o valor na variavel
    elif sabor == "AC" and tamanho == "G":
        print ("Você pediu um açai no tamanho G: R$ 20.00\n")     #Tamanho G Açai
        preco += 20 #Acumulando o valor na variavel
    i = input("Deseja mais alguma coisa ? [S] / [N] : ") .upper()  #Input para continuar o pedido (Exigencia 06 / 08)
    if i == "N":
        break # Se o input for "N", acaba o programa, se não ele repete o pedido"
    else:
        continue 
print (f"\nSeu pedido deu R$ {preco:.2f}") #Mensagem mostrando o valor e agradecendo
print ("Obrigado por pedir conosco, volte sempre")
    




