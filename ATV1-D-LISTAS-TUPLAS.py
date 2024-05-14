def cadastrar_livro(id_global): #Função cadastrar livro
    livro = {} #Dicionario criado
    print ("-----------------------")
    id_livro = int(input ("Digite o ID do livro: ")) 
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o nome do autor: ")
    editora = input("Digite o nome da editora: ")
    #Passando todas informações para o dicionario
    livro['id'] = id_livro 
    livro['nome'] = nome
    livro['autor'] = autor
    livro['editora'] = editora
    print("Livro cadastrado com sucesso")
    lista_livros.append(livro) #Adicionei o dicionario ao final da lista livros 
    return lista_livros, livro # Retornei as informaçoes

def consultar_livro(lista_livros):  #Exigencia 03 = Funcão consultar livro 
    print("-------MENU-CONSULTA-LIVRO--------")
    print("Escolha a opção desejada:")
    #Pergunta a opção desejada - A
    print("1 - Consultar todos os livros")
    print("2 - Consultar livro por ID")
    print("3 - Consultar livro por Autor")
    print("4 - Retornar")
    opcao = input(">>> ")

    if opcao == "1":
        if lista_livros:
            #Consultando todos os livros aparecem todos com o FOR 
            print("Lista dos livros:")
            for livro in lista_livros:
                print(f"ID: {livro['id']}")
                print(f"Nome: {livro['nome']}")
                print(f"Autor: {livro['autor']}")
                print(f"Editora: {livro['editora']}")
                print("-----------------------")
        else:
            print("Não há livros cadastrados.") #caso consulte e não tenham livros cadastrados

    elif opcao == "2":
        id_consulta = int(input("Digite o ID do Livro: ")) #Consultando por ID
        livro_encontrado = False #variavel para saber se o livro foi encontrado
        for livro in lista_livros: #Checa em todas informaçoes da lista de livros
            if livro['id'] == id_consulta: #Se os IDS forem iguais, printa as informaçoes e segue
                print("Livro encontrado:")
                print(f"ID: {livro['id']}")
                print(f"Nome: {livro['nome']}")
                print(f"Autor: {livro['autor']}")
                print(f"Editora: {livro['editora']}")
                livro_encontrado = True #Livro é true caso os ids sejam iguais
                break #Acaba aqui
        if not livro_encontrado: #Se não achar da erro (acho que talvez daria pra usar try except)
            print(f"Livro com o ID {id_consulta} não encontrado.")

    elif opcao == "3":
        autor_consulta = input("Qual o nome do autor? ") #Consultando por autor
        livros_encontrados = False 
        for livro in lista_livros: 
            if livro["autor"] == autor_consulta: 
                print(f"ID: {livro['id']}")
                print(f"Nome: {livro['nome']}")
                print(f"Autor: {livro['autor']}")
                print(f"Editora: {livro['editora']}")
                livros_encontrados = True
        if not livros_encontrados:
            print("Não há livros cadastrados deste autor.")

    elif opcao == "4":
        print("Retornando ao menu principal.") #Se for a opcao 4, apenas retorna ao menu principal
        return

    else: #caso não seja nenhuma das outras, opçaõ é invalida
        print("Opção inválida")         

def remover_livro(lista_livros): #Exigencia 05 - Função remover livros
    print("--------Menu remover livro---------")
    while True: 
        idremover = int(input("Qual o ID do livro a ser removido?\n[0] para voltar ao menu principal: ")) #Pergunta o ID do livro, e avisa que se apertar 0 volta ao menu principal (Coloquei isso pq acabei ficando em um loop infinito quando entrei nesse menu sem livros cadastrados)
        if idremover == 0: #Se for 0, volta ao menu principal
            break  
        
        livro_encontrado = False
        for livro in lista_livros:
            if livro["id"] == idremover:
                lista_livros.remove(livro)
                livro_encontrado = True
                print("Livro removido com sucesso")
                break
        if not livro_encontrado:
            print("ID inválido, tente novamente por favor")

id_global = 1 #Exigencia 02, ID global criado
lista_livros = []  #lista de dicionarios
print ("----------SEJA-BEM-VINDO----------") #Exigencia 01, mensagem de boas vindas com meu nome logo abaixo
while True: #Coloquei a mensagem fora do loop para aparecer apenas na primeira execução
    print("------BIBLIOTECA DO BRENINHO------")
    print("----------MENU PRINCIPAL----------")
    print("Escolha a opção desejada:")
    print("1 - Cadastrar livro")
    print("2 - Consultar livro(s)")
    print("3 - Remover livro")
    print("4 - Sair")

    opcao = input(">>> ")
    #Estrutura de IFS-ELIFS-ELSE para todas exigencias 06
    if opcao == "1":
        lista_livros, _ = cadastrar_livro(id_global) #posso ter criado uma variavel a mais, porem no exemplo pedia para poder escrever o ID do livro também 
    elif opcao == "2":
        consultar_livro(lista_livros)
    elif opcao == "3":
        remover_livro(lista_livros)
    elif opcao == "4":
        print("Saindo do aplicativo")
        break
    else:
        print("Opção inválida")