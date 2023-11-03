#criação de um menu para o usuario selecionar qual setor ele quer conferir
def menu_opcao():
  print("\nBem vindo(a) ao IF Administra! Qual estoque você deseja entrar?\n 1-Cooperativa\n 2-Refeitorio\n 3-Agroindustria\n 4-Sair do programa")
  while True: #validar a opção do input
    try:
      op = int(input("\nDigite a opção desejada: "))
    except:
      print("\nVocê digitou uma letra. Por favor digite apenas número.\n")
    else:
      return op

def cooperativa(): #menu de opções da coooperativa
    print(" \nCooperativa! O que você deseja fazer?\n 1-Ver estoque\n 2-Adicionar item\n 3-Remover item\n 4-Voltar ao menu principal:")
    while True:
     try:
        op = int(input("\nDigite a opção desejada: "))
     except:
        print("\nVocê digitou uma letra. Por favor digite apenas número.\n")
     else:
        return op

def refeitorio(): #menu de opções do refeitorio
    print(" \nRefeitório! O que você deseja fazer?\n 1-Ver estoque\n 2-Adicionar item\n 3-Remover item\n 4-Voltar ao menu principal:")
    while True:
     try:
        op = int(input("\nDigite a opção desejada: "))
     except:
        print("\nVocê digitou uma letra. Por favor digite apenas número.\n")
     else:
        return op

def agroindustria(): #menu de opções do agroindustria
    print(" \nAgroindústria! O que você deseja fazer?\n 1-Ver estoque\n 2-Adicionar item\n 3-Remover item\n 4-Voltar ao menu principal:")
    while True:
     try:
        op = int(input("\nDigite a opção desejada: "))
     except:
        print("\nVocê digitou uma letra. Por favor digite apenas número.\n")
     else:
        return op

#Codigo
#Obs: acho que se tirasse o menu_opção do match e deixasse só os outros menus, teria como deixar eles infinitos
while True: #Deixar o programa rodando infinitamente, ao menos que escolha a opção para sair do programa
   match menu_opcao():
         case 1:
            while True:
               match cooperativa():
                  case 1:
                        dados_colunas=[]
                        dados_linhas=[]
                        dados_final=[]
                        with open("cooperativa_log.txt","r") as arquivo: #leitura do arquivo e mostra o estoque detro dele
                           conteudo= arquivo.read()
                           dados_colunas= conteudo.split(";") #separar os dados em colunas, coloquei ";" pois estava dando conflito (com uma parte posterior do código) quando utilizava "\n"
                           for linha in dados_colunas: #percorre a matriz "dados_colunas"
                              dados_linhas= linha.split(",") #separar as colunas em linhas
                              dados_final.append(dados_linhas)
                        print(f'\nO estoque contém:')
                        for linha in dados_final: #mostrar a matriz
                           print(linha)
                  case 2:
                    estoque={}
                    item=input("digite o item a ser adicionado ao estoque: ")
                    quantidade=int(input("digite a quantidade desse item: "))
                    # convertendo arquivo em dicionario
                    with open("cooperativa_log.txt","r") as arquivo: #leitura do arquivo e mostra o estoque detro dele
                        conteudo= arquivo.read()
                        conteudo= conteudo[1:-1] #remove os cochetes de abertura e fechamento do arquivo.
                        print(conteudo)
                        pares = conteudo.split(", ") #divide o texto em pares separados por ,
                        for par in pares:
                          chave, valor = par.split(": ") #separa a string do valor
                          estoque[chave.strip("'")] = int(valor) #adiciona a chave e o valor ao dicionario removendo a aspas simples e so aceitando valores inteiros
                    estoque[item]=quantidade
                    #convertendo dicionario em string e atualizando arquivo de texto.
                    converter_para_string= str(estoque)
                    with open('cooperativa_log.txt', 'w') as arquivo:
                        arquivo.write(converter_para_string)
                  case 3:
                     conteudo = {}
                     deletar= input("digite o item a ser excluido do estoque: ")
                     with open('cooperativa_log.txt', 'r') as arquivo:
                        for linha in arquivo: #Para cada linha no arquivo, dividimos a linha em pares separados por ponto e vírgula.
                           pares = linha.strip().split(';')
                           for par in pares:
                                 chave, valor = par.split(',')#dividimos cada par em chave e valor, separados por vírgula
                                 conteudo[chave] = int(valor)#Convertemos o valor para um número inteiro
                     consulta= deletar in conteudo
                     if consulta == True:
                      del conteudo[deletar]
                      convetido= str(conteudo)# convertendo dicionario em string para salvar em arquivo
                     with open('cooperativa_log.txt', 'w') as arquivo:
                        arquivo.write(convetido)
                        #o arquivo fica salvo com os cochetes do dicionario, arrumar uma forma para remover isso ou muda o codigo de matriz para dicionario
                  case 4:
                     print("\nDesligando sistema. Obrigado por utilizá-lo ^^")
                     break
                                 
         case 4:
            print("\nDesligando sistema. Obrigado por utilizá-lo ^^")
            break

         case _:
            print("\nOpção inválida")