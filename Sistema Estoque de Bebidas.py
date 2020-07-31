# Todas as Variáveis

escolha = 0
cod = 0
menuPrincipal = 0
menuCadastrar = 0
menuControle = 0
quantidadeAntiga = 0
produtoEntrada = 0
produtoSaida = 0
VendaAntiga = 0
lucroObtidoTotal = 0

# Cabeçalho
#------------------------------
#            TEXTO
#------------------------------

def linha(tam=46):
    return '-' * tam

def cabecalho(txt):
    print("")
    print(linha())
    print(txt.center(46))
    print(linha())
    print("")
# Fim do cabeçalho

#Funções

# Mostrar os dados

def mostrarDados():
    mostrar = "------------------------\n\n"
    print("\n------------------------")
    print("Cód.:", listaCodigo[cod])
    print("Nome:", listaNome[cod])
    print("Quantidade:", listaQuantidade[cod])
    print("Modelo: ", listaModelo[cod])
    print("Fabricante: ", listaFabricante[cod])
    print("Valor de custo:", listaCusto[cod])
    print("Valor de venda:", listaVenda[cod])
    return mostrar

# Função para nenhum produto cadastrado

def nenhum_produto_cadastrado():
    if listaNome == []:
        nenhumNome = print ("Nenhum produto cadastrado")
    return nenhumNome

# Listas necessárias

listaNome = []
listaCodigo = []
listaQuantidade = []
listaQuantidadeAntiga = []
listaSaida = []
listaEntrada = []
listaModelo = []
listaFabricante = []
listaCusto = []
listaCustoAntigo = []
listaVenda = []
listaVendaAntiga = []
    
# Laço de repetição do menu principal

while True:
    cabecalho("CONTROLE DE ESTOQUE DE BEBIDAS")
    menuPrincipal = (input("1. Tela de Cadastro\n2. Tela de Consulta\n3. Controle de estoque\n4. Sair\n\nDigite uma opção: "))
    print("\n------------------------")

#1   # Menu de cadastro onde existe uma condições para a escolha do menu do usuário # 1

    if(menuPrincipal == "1"):
        while True:
            menuCadastrar = (input("1. Novo produto\n2. Alterar produto\n3. Remover produto\n4. Retornar ao Menu Inicial\n\nDigite uma opção: "))
            print("\n")

            
#   #   # Menu para cadastrar um novo produto # 1.1

            if (menuCadastrar == "1"):
                
                while True:
                        # Limite total da quantidade de produtos cadastrados
                    if (len(listaNome)) == 10000:
                        cabecalho("Capacidade máxima de produtos excedida! Por favor, contate um desenvolvedor para que aumente o limite")
                        break
                    
                    while True:
                        # Cadastrar nome do produto
                        print(linha())
                        nomeDigitado = input("Digite o Nome do Produto: ")

                        # Se o usuário digitar nome vazio
                        if(nomeDigitado == ""):
                            cabecalho("Nome inválido, tente novamente!")

                        # Se produto ja estiver na lista
                        elif (nomeDigitado in listaNome):
                            cabecalho("Nome ja cadastrado, tente novamente!")

                        #Verificar se existe somente letras ou hífens
                        else:
                            # Range retorna uma lista no intervalo definido
                            # Len retorna a quantidade de elementos de qualquer lista
                            for i in range(len(nomeDigitado)):
                                         
                                if (ord(nomeDigitado[i])) in range(65,91) or (ord(nomeDigitado[i])) in range(97,123) or ord(nomeDigitado[i]) == 45 or ord(nomeDigitado[i]) == 231 or ord(nomeDigitado[i]) == 32:
                                    continue

                                else:                                   
                                    cabecalho("Nome do produto só pode conter letras e hífens")
                                    break

                        # Condição para avançar pra proxima etapa
                            if (ord(nomeDigitado[i])) in range(65,91) or (ord(nomeDigitado[i])) in range(97,123) or ord(nomeDigitado[i]) == 45 or ord(nomeDigitado[i]) == 231 or ord(nomeDigitado[i]) == 32:
                                break
                                                            
                                     
                    # Adicionar nome do produto na lista
                    listaNome.append(nomeDigitado)
                        
                    # Cadastrar quantidade de um produto na lista.
                    while True:
                        quantidadeDigitado = (input("Digite a quantidade do produto: "))

                        # Se o usuário digitar nome vazio
                        if(quantidadeDigitado == ""):
                            cabecalho("Quantidade inválida, tente novamente!")

                        # Verificar se há somente números
                        else:
                            # Range retorna uma lista no intervalo definido
                            # Len retorna a quantidade de elementos de qualquer lista
                            for i in range(len(quantidadeDigitado)):
                                         
                                if (ord(quantidadeDigitado[i])) in range(48,58):
                                    continue

                                else:                                   
                                    cabecalho("Quantidade do produto só pode conter números")
                                    break
                            

                            # Condição para avançar pra próxima etapa
                            if (ord(quantidadeDigitado[i])) in range(48,58):

                                int(quantidadeDigitado)
                                break

                    # Adicionar quantidade na lista             
                    listaQuantidade.append(quantidadeDigitado)
                    
                    quantidadeAntiga = quantidadeDigitado
                    listaQuantidadeAntiga.append(quantidadeAntiga)

                            
                    # Acicionar o modelo do produto na lista
                    while True:
                        modeloDigitado = (input("Digite o modelo do produto: "))

                        if(modeloDigitado == ""):
                            cabecalho("Modelo inválido, tente novamente!")
                        else:
                            listaModelo.append(modeloDigitado)
                            break

                    # Acicionar o modelo do produto na lista
                    while True:
                        fabricanteDigitado = (input("Digite o fabricante do produto: "))

                        if(fabricanteDigitado == ""):
                            cabecalho("Fabricante inválido, tente novamente!")
                        else:
                            listaFabricante.append(fabricanteDigitado)
                            break
                    

                    # Adicionar o valor de custo de um produto na lista.                        
                    while True:
                        custoDigitado = (input("Digite o valor de custo do produto: "))

                        # Se o usuário digitar nome vazio
                        if(custoDigitado == ""):
                            cabecalho("Valor inválido!")
                        
                        # Verificar se há somente números
                        else:
                            for i in range(len(custoDigitado)):
                                         
                                if (ord(custoDigitado[i])) in range(48,58) or (ord(custoDigitado[i])) == 46:
                                    continue
                                else:
                                    cabecalho("Somente é permitido números!")
                                    break
                          

                            # Condição para avançar pra próxima etapa
                            if (ord(custoDigitado[i])) in range(48,58):

                                float(custoDigitado)
                                break
                            
                            if (ord(custoDigitado[i])) in range(46,47):

                                float(custoDigitado)
                                break
                          
                    # Adicionar custo do produto na lista
                    listaCusto.append(custoDigitado)
                    
                    custoAntigo = custoDigitado
                    listaCustoAntigo.append(custoAntigo)
                    

                    # Adicionar o valor de venda de um produto na lista.
                    while True:
                        vendaDigitado = (input("Digite o valor de venda do produto: "))

                        # Se o usuário digitar nome vazio
                        if(vendaDigitado == ""):
                            cabecalho("Valor inválido!")

                        
                        # Verificar se há somente numeros
                        else:
                            for i in range(len(vendaDigitado)):
                                         
                                if (ord(vendaDigitado[i])) in range(48,58) or (ord(vendaDigitado[i])) == 46:
                                    continue
                                else:
                                    cabecalho("valor inválido!")
                                    break
                          

                            # Condição para avançar pra próxima etapa
                            if (ord(vendaDigitado[i])) in range(48,58):

                                float(vendaDigitado)
                                break
                            
                            if (ord(vendaDigitado[i])) in range(46,47):

                                float(vendaDigitado)
                                break
                    
                    # Adicionar valor de venda do produto na lista
                    listaVenda.append(vendaDigitado)
                    
                    VendaAntiga = vendaDigitado
                    listaVendaAntiga.append(VendaAntiga)
                    

                    # Adicionar o código do produto em uma lista
                    listaCodigo.append((len(listaCodigo)))


                    # Menssagem de exito
                    cabecalho("Produto cadastrado com sucesso!")

                    break

#   #   #Menu para alterar um produto # 1.2
            elif (menuCadastrar == "2"): 

                # Quando não há nenhum produto cadastrado               
                if (listaNome == []):
                    cabecalho("Nenhum produto cadastrado")
                

                # Listar produtos cadastrados
                else:                    
                    while True:
                        print("Lista de produtos cadastrados")
                        for i in range(len(listaCodigo)):            
                            print(listaCodigo[i]," --- ",listaNome[i])
                        print("\n\n")

                        
                        cod = int(input("Digite o código do produto: "))
                       
                                 
                        # Se o usuário digitar valor vazio 
                        if (cod == ""):
                            cabecalho ("Valor inválido,tente novamente!")

                                                    
                        # Se o que foi digitado não estiver contido na lista 
                        elif (cod not in listaCodigo):
                            cabecalho ("Valor invalido ou produto não cadastrado!")                
                                                   
                        # Mostrar dados especificos do produto
                        else:
                            print(mostrarDados())
                            print("Deseja alterar os dados exibidos?")
                            escolha = (input("1. Sim\n2. Não\n\nDigite uma opção: "))

                            while True:

#   #   #   #Condição de seguraça para alterar o produto # 1.2.1
                                if (escolha == "1"): 

                                    # Excluir o indice especifico do produto digitado
                                    listaNome.pop(cod)                
                                    listaQuantidade.pop(cod)
                                    listaModelo.pop(cod)
                                    listaFabricante.pop(cod)
                                    listaCusto.pop(cod)
                                    listaVenda.pop(cod)
                                    listaCodigo.pop(cod)
                                    
                                    # Alterar nome do produto na lista
                                    while True:
                                        # Cadastrar nome do produto
                                        print(linha())
                                        nomeDigitado = input("Digite o nome do produto: ")

                                        # Se o usuário digitar nome vazio
                                        if(nomeDigitado == ""):
                                            cabecalho("Nome inválido, tente novamente!")

                                        # Se produto ja estiver condito na lista
                                        elif (nomeDigitado in listaNome):
                                            cabecalho("Nome ja cadastrado, tente novamente!")

                                        # Verificar se há somente letras
                                        else:
                                            for i in range(len(nomeDigitado)):
                                                         
                                                if (ord(nomeDigitado[i])) in range(65,91) or (ord(nomeDigitado[i])) in range(97,123) or ord(nomeDigitado[i]) == 45 or ord(nomeDigitado[i]) == 231:
                                                    continue

                                                else:                                   
                                                    cabecalho("Nome do produto só pode conter letras e hífens")
                                                    break

                                        # Condição para avançar pra proxima etapa
                                            if (ord(nomeDigitado[i])) in range(65,91) or (ord(nomeDigitado[i])) in range(97,123) or ord(nomeDigitado[i]) == 45 or ord(nomeDigitado[i]) == 231:
                                                break
                                                                            
                                                     
                                    # Inserir nome do produto na lista
                                    listaNome.insert(cod,nomeDigitado)
                                        
                                
                                    # Cadastrar quantidade de um produto a uma lista.
                                    while True:
                                        quantidadeDigitado = (input("Digite a quantidade do produto: "))

                                        # Se o usuário digitar nome vazio
                                        if(quantidadeDigitado == ""):
                                            cabecalho("Quantidade inválida, tente novamente!")

                                        
                                        # Verificar se há somente numeros
                                        else:
                                            for i in range(len(quantidadeDigitado)):
                                                         
                                                if (ord(quantidadeDigitado[i])) in range(48,58):
                                                    continue

                                                else:                                   
                                                    cabecalho("Quantidade do produto só pode conter números")
                                                    break
                                            

                                            # Condição para avançar pra proxima etapa
                                            if (ord(quantidadeDigitado[i])) in range(48,58):

                                                int(quantidadeDigitado)
                                                break

                                    # Inserir quantidade na lista             
                                    listaQuantidade.insert(cod,quantidadeDigitado)
                                            
                                    quantidadeAntiga = quantidadeDigitado
                                    listaQuantidadeAntiga.insert(cod,quantidadeAntiga)

                                            
                                    # Inserir o modelo do produto na lista
                                    
                                    modeloDigitado = (input("Digite o modelo do produto: "))
                                    listaModelo.insert(cod,modeloDigitado)

                                    # Inserir o modelo do produto na lista
                                    
                                    fabricanteDigitado = (input("Digite o fabricante do produto: "))
                                    listaFabricante.insert(cod,fabricanteDigitado)
                                    

                                    # Adicionar o valor de custo de um produto na lista.                        
                                    while True:
                                        custoDigitado = (input("Digite o valor de custo do produto: "))

                                        # Se o usuário digitar nome vazio
                                        if(custoDigitado == ""):
                                            cabecalho("Valor inválido, tente novamente!")
                                        
                                        # Verificar se há somente numeros
                                        else:
                                            for i in range(len(custoDigitado)):
                                                         
                                                if (ord(custoDigitado[i])) in range(48,58) or (ord(custoDigitado[i])) == 46:
                                                    continue
                                                else:
                                                    cabecalho("valor inválido, somente números permitidos!")
                                                    break
                                          

                                            # Condição para avançar pra proxima etapa
                                            if (ord(custoDigitado[i])) in range(48,58):

                                                float(custoDigitado)
                                                break
                                            
                                            if (ord(custoDigitado[i])) in range(46,47):

                                                float(custoDigitado)
                                                break
                                          
                                    # Inserir custo do produto na lista           
                                    listaCusto.insert(cod,custoDigitado)
                                    
                                    custoAntigo = custoDigitado
                                    listaCustoAntigo.insert(cod,custoAntigo)
                                    

                                    # Adicionar o valor de venda de um produto na lista.
                                    while True:
                                        vendaDigitado = (input("Digite o valor de venda do produto: "))

                                        # Se o usuário digitar nome vazio
                                        if(vendaDigitado == ""):
                                            cabecalho("Valor inválido, tente novamente!")

                                        
                                        # Verificar se há somente numeros
                                        else:
                                            for i in range(len(vendaDigitado)):
                                                         
                                                if (ord(vendaDigitado[i])) in range(48,58) or (ord(vendaDigitado[i])) == 46:
                                                    continue
                                                else:
                                                    print("valor inválido, somente números!")
                                                    break
                                          

                                            # Condição para avançar pra proxima etapa
                                            if (ord(vendaDigitado[i])) in range(48,58):

                                                float(vendaDigitado)
                                                break
                                            
                                            if (ord(vendaDigitado[i])) in range(46,47):

                                                float(vendaDigitado)
                                                break
                                    # Inserir valor de venda do produto na lista           
                                    listaVenda.insert(cod,vendaDigitado)
                                    
                                    VendaAntiga = vendaDigitado
                                    listaVendaAntiga.insert(cod, VendaAntiga)
                                    

                                    # Inserir o código do produto em uma lista
                                    listaCodigo.insert(cod,cod)


                                    # Menssagem de exito
                                    cabecalho("Produto alterado com sucesso!")

                                    break
                                break
                            break

#   #   # Remover produto cadastrado  # 1.3
            elif (menuCadastrar == "3"):

                # Quando não há nenhum produto cadastrado 
                if (listaNome == []):
                    cabecalho("Nenhum produto cadastrado")

                # Listar produtos cadastrados
                else:
                    while True:

                        # For que mostrar os produtos
                        print("Lista de produtos cadastrados")
                        for i in range(len(listaCodigo)):            
                            print(listaCodigo[i]," --- ",listaNome[i])
                        print("\n\n")
                    
                        cod = int(input("Digite o código do produto: "))

                        # Valor não contido dentro da lista de codigos
                        if cod not in listaCodigo:
                            cabecalho("Valor invalido ou produto não cadastrado")                        
                        
                        else:
                            # Mostrar dados especificos do produto
                            print(mostrarDados())
                            print("Deseja excluir os dados exibidos?")
                            escolha = (input("1. Sim\n2. Não\n\nDigite uma opção: "))

                            

                            # Condição de seguraça para excluir o produto # 1.3.1
                            if(escolha == "1"):

                                # Excluir o indice especifico do produto digitado
                                listaNome.pop(cod)                
                                listaQuantidade.pop(cod)
                                listaModelo.pop(cod)
                                listaFabricante.pop(cod)
                                listaCusto.pop(cod)
                                listaVenda.pop(cod)
                                listaCodigo.pop(cod)
                                
                                
                                
                                # Menssagem de exito
                                cabecalho("Produto excluido com sucesso!")
                                break

                            # Não excluir o produto
                            elif(escolha == "2"):
                                print(linha)
                                break

                            # Se o usuário digitar valor vazio
                            elif(escolha == ""):
                                cabecalho("Valor invalido ou produto não cadastrado")

                            # Se o usuário digitar caracter invalidos
                            else:
                                cabecalho("Valor invalido ou produto não cadastrado")
                    break
                
                            
#   #   # Retornar ao menu principal # 1.4
            elif (menuCadastrar == "4"):
                menuCadastrar = 0
                break

#   #   # Condição caso o usuario digite um numero errado
            else:
                cabecalho("O número ou caracter digitado é inválido.\nPor favor, tente novamente")
            

#   # Consultar um produto # 2    
    elif(menuPrincipal == "2"):
        while True:
            if (listaNome == []):
                cabecalho("Nenhum produto cadastrado")
                    
            else:
                while True:
                    
                    print("Lista de produtos cadastrados")
                    for i in range(len(listaCodigo)):            
                        print(listaCodigo[i]," --- ",listaNome[i])
                    print("\n\n")

                    cod = int(input("Digite o código do produto: "))

                    if (cod not in listaCodigo):
                        cabecalho("Valor invalido ou produto não cadastrado")

                    else:
                        
                        print(mostrarDados())
                    break
                        
            break


#   # Controlar estoque # 3
    elif(menuPrincipal == "3"):
        while True:
            print(linha())
            menuControle = input("1. Registrar entrada de produtos\n2. Registrar saída de produtos\n3. Saldo de estoque unitário\n4. Total de estoque\n5. Voltar ao menu principal\n\nDigite uma opção: ")

#   #   #   # Registrar entrada de produtos #3.1
            if (menuControle == "1"):
                if (listaNome == []):
                    cabecalho("Nenhum produto cadastrado")

                # Listar produtos cadastrados
                else:
                    while True:

                        # For que tem a função de mostrar os produtos
                        print("Lista de produtos cadastrados")
                        for i in range(len(listaCodigo)):            
                            print(listaCodigo[i]," --- ",listaNome[i])
                        print("\n\n")
                    
                        cod = int(input("Digite o código do produto: "))

                        # Valor não contido dentro da lista de codigos
                        if cod not in listaCodigo:
                            cabecalho("Valor invalido ou produto não cadastrado")                     
                        
                        else:
                            # Mostrar dados especificos do produto
                            print(mostrarDados())
                            print("Deseja alterar a quantidade de produto exibido?")
                            escolha = (input("1. Sim\n2. Não\n\nDigite uma opção: "))

                            

                            # Condição de seguraça para excluir o produto
                            if(escolha == "1"):

                                # Alterar oa quantia do produto digitado                                                
                                quantidade_adicionada = int(input("Digite a quantidade que deseja registrar: "))
                                quantidade_nova = int(listaQuantidade[cod]) + quantidade_adicionada
                                
                                listaQuantidade.pop(cod)
                                listaQuantidade.insert(cod, quantidade_nova)

                                produtoEntrada += quantidade_adicionada 
                                listaEntrada.insert(cod, produtoEntrada)

                                
                                # Menssagem de exito
                                cabecalho("Quantidade registrada com sucesso!")
                                break

                            # Não excluir o produto
                            elif(escolha == "2"):
                                print("-----------------------------\n")
                                break

                            # Se o usuário digitar valor vazio
                            elif(escolha == ""):
                                cabecalho("Valor invalido ou produto não cadastrado")                               

                            # Se o usuário digitar caracter invalidos
                            else:
                                cabecalho("Valor invalido ou produto não cadastrado")
                    break
                
                
#   #   #   # Registrar saída de produtos # 3.2

            elif (menuControle == "2"):
                if (listaNome == []):
                    cabecalho("Nenhum produto cadastrado")

                # Mostrar produtos cadastrados
                else:
                    while True:

                        # For que tem a função de mostrar os produtos
                        print("Lista de produtos cadastrados")
                        for i in range(len(listaCodigo)):            
                            print(listaCodigo[i]," --- ",listaNome[i])
                        print("\n\n")
                    
                        cod = int(input("Digite o código do produto: "))

                        # Valor não contido dentro da lista de codigos
                        if cod not in listaCodigo:
                            cabecalho("Valor invalido ou produto não cadastrado")                       
                        
                        else:
                            # Mostrar dados especificos do produto
                            print(mostrarDados())
                            print("Deseja alterar a quantidade de produto exibido?")
                            escolha = (input("1. Sim\n2. Não\n\nDigite uma opção: "))

                            

                            # Condição de seguraça para excluir o produto
                            if(escolha == "1"):

                                # Alterar a quantia do produto digitado
                                print("\n---------------------------------------")
                                quantidade_removida = int(input("Digite a quantidade que deseja remover: "))
                                      
                                quantidade_nova = int(listaQuantidade[cod]) - quantidade_removida
                                
                                listaQuantidade.pop(cod)
                                listaQuantidade.insert(cod, quantidade_nova)

                                produtoSaida += quantidade_removida 
                                listaSaida.insert(cod, produtoSaida)

                                                                
                                # Menssagem de exito
                                if(escolha == "1"):
                                    cabecalho("Baixa de produto concluida com sucesso!")
                                    break

                            # Não excluir o produto
                            elif(escolha == "2"):
                                print("-----------------------------\n")
                                break

                            # Se o usuário digitar valor vazio
                            elif(escolha == ""):
                                cabecalho("Valor invalido ou produto não cadastrado")                             

                            # Se o usuário digitar caracter invalidos
                            else:
                                cabecalho ("Valor invalido ou produto não cadastrado")
                    break
#   #   #   # Saldo de estoque unitário # 3.3
            elif (menuControle == "3"):
                if (listaNome == []):
                    cabecalho("Nenhum produto cadastrado")

                # Listar produtos cadastrados
                else:
                    while True:

                        # For que mostrar os produtos
                        print("Lista de produtos cadastrados")
                        for i in range(len(listaCodigo)):            
                            print(listaCodigo[i]," --- ",listaNome[i])
                        print("\n\n")
                    
                        cod = int(input("Digite o código do produto: "))

                        # Valor não contido dentro da lista de codigos
                        if cod not in listaCodigo:
                            cabecalho("Valor invalido ou produto não cadastrado")                      
                        
                        else:
                            # Printar dados especificos do produto
                                                      
                            print("\n------------------------")
                            print("Cód.:", listaCodigo[cod])
                            print("Nome:", listaNome[cod])
                            print("Quantidade inicial: ", listaQuantidadeAntiga[cod])
                            print("Quantidade atual: ", listaQuantidade[cod])
                            print("------------------------\n")
                            
                                                         
                            break                        
                    
#   #   #   # Análise total de estoque # 3.4
            elif (menuControle == "4"):

                if (listaNome == []):
                    cabecalho("Nenhum produto cadastrado")

                else:
                    # For que mostrar os produtos
                    print("\n-------------------------------------")
                    print("Lista de produtos cadastrados")
                    for i in range(len(listaCodigo)):            
                        print(listaCodigo[i]," --- ",listaNome[i], " --- Quant. disponível: ",listaQuantidade[i])
                    print("-------------------------------------\n")
            

                   


#   #   #   # Retornar ao menu principal # 3.6
            elif(menuControle == "5"):
                break

            # Condição caso o usuario digite um numero errado
            else:
                cabecalho("O número ou caracter digitado é inválido.\nPor favor, tente novamente.")

    
#   # Condição do while, se o menu for diferente de 4 ele continua, caso contrario ele encerra e manda uma mensagem    
    elif(menuPrincipal == "4"):
        print("Obrigado por usar nosso programa, volte sempre!")
        break

#   # Condição caso o usuario digite um numero errado
    else:
        cabecalho("O número ou caracter digitado é inválido.\nPor favor, tente novamente.")
