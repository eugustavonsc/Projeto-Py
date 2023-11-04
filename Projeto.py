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
while True: #Deixar o programa rodando infinitamente, ao menos que escolha a opção para sair do programa
   match menu_opcao():
         case 1:
            while True:
               match cooperativa():
                  case 1:
                     with open("cooperativa_log.txt","r") as arquivo: #leitura do arquivo e mostra o estoque detro dele
                        conteudo= arquivo.read()
                        conteudo= conteudo[1:-1] #remove os cochetes de abertura e fechamento do arquivo.
                        pares = conteudo.split(", ") #divide o texto em pares separados por ,
                        for par in pares:
                           print(par)
                  case 2:
                     estoque={}
                     item=input("Digite o item a ser adicionado ao estoque: ")
                     while True:
                        try:
                           quantidade = int(input("\nDigite a quantidade desse item: "))
                        except:
                           print("\nVocê digitou uma letra. Por favor digite apenas número.")
                        else:
                           break
                     # convertendo arquivo em dicionario \/
                     with open("cooperativa_log.txt","r") as arquivo: #leitura do arquivo e mostra o estoque detro dele
                        conteudo= arquivo.read()
                        conteudo= conteudo[1:-1] #remove os cochetes de abertura e fechamento do arquivo.
                        pares = conteudo.split(", ") #divide o texto em pares separados por ,
                        for par in pares:
                           chave, valor = par.split(": ") #separa a string do valor
                           estoque[chave.strip("'")] = int(valor) #adiciona a chave e o valor ao dicionario removendo a aspas simples e so aceitando valores inteiros
                     estoque[item]=quantidade
                     #convertendo dicionario em string e atualizando arquivo de texto.
                     converter_para_string= str(estoque)
                     with open('cooperativa_log.txt', 'w') as arquivo:
                        arquivo.write(converter_para_string)
                     print(f"O seu item {item} foi adicionado com a quantidade {quantidade} no sistema!")
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