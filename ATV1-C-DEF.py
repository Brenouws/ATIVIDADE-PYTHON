def escolha_servico():   #Função escolha serviço exigencia 02/07
    preco_servico = 0
    print("Qual o tipo de serviço desejado?")   # A - Pergunta o serviço desejado 
    print("DIG - Digitalização")
    print("ICO - Impressao colorida")
    print("IPB - Impressao preto e branco")
    print("FOT - Fotocopia")
    servico = input(">>> ") # B - Retorna o valor servico com base na escolha do usuario 
    while servico not in ["DIG", "ICO", "IPB", "FOT"]: # C - Repete B . A se digitar uma opção diferente
        print("Escolha inválida, entre com o tipo do serviço novamente")
        servico = input(">>> ")
        
    if servico == "DIG":
        preco_servico += 1.10
    elif servico == "ICO":
        preco_servico += 1
    elif servico == "IPB":
        preco_servico += 0.40
    elif servico == "FOT":
        preco_servico += 0.20
    
    return preco_servico

def num_pag(): # Deve se implementar a função num_pag exigencia 03/07
    while True:
        try: # c. Repete a pergunta do item C.a se digitar um valor acima de 20000 ou valor não numérico (use try/except para não numérico
            pags = input("Quantas páginas serão? ") # a. Pergunta o número de páginas;
            pags = int(pags)
            desconto = 0
            if pags >= 20 and pags < 200: # b. Retorna o número de páginas com desconto seguindo a regra do enunciad
                desconto = pags / 100 * 15
                pags = pags - desconto
            elif pags >= 200 and pags < 2000:
                desconto = pags / 100 * 20
                pags = pags - desconto
            elif pags >= 2000 and pags < 20000:
                desconto = pags / 100 * 25
                pags = pags - desconto
            if pags >= 20000:
                print("Não aceitamos pedidos com mais de 20.000 páginas")
                continue
            break
        except ValueError: # Exigencia de codigo 06 de 07 deve-se implementar try/except
            print("Por favor, insira um valor válido")
    return pags
    return desconto

def servico_extra(): # Deve-se implementar a função servico_extra() # Exigencia de codigo 4 de 7
    extra = 0
    while True: # c. Repetir a pergunta item D.a se digitar uma opção diferente de: 1/2/0;
        print("Deseja adicionar mais algum serviço?") # a. Pergunta pelo serviço adicional;
        print("1 - Encadernação simples - R$ 15,00") 
        print("2 - Encadernação capa dura - R$ 40,00")
        print("0 - Não desejo mais nada.")
        opcao = input(">>> ")
        if opcao == "1":
            extra += 15
            break
        elif opcao == "2":
            extra += 40
            break
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida")
    return extra    #b. Retornar o valor de apenas uma das opções de adicional


print("Bem-vindo à copiadora do Breninho") # Exigencia de codigo 01/07 mensagem de boas vindas com meu nome
preco_servico = escolha_servico()  #Chamando a função para pegar o preco do servico
pags = num_pag() #Funcão para pegar a quantidade de paginas 
extra = servico_extra()
total = (preco_servico * pags) + extra 
print(f"O valor final foi de R$ {total:.2f} (SERVICO : {preco_servico:.2f} * páginas: {pags} + extra: {extra})") # Deve-se implementar o total a pagar no código principal (main), ou seja, não pode estar dentro de função, conforme o enunciado Exigencia 05/07
