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
                        with open("cooperativa_log.txt","a") as arquivo: #leitura do arquivo e mostra o estoque detro dele
                           Item=input("Digite o item a ser adicionado ao estoque: ")
                           arquivo.write(f";{Item}") #adicionar o Item no arquivo
                           while True: #validar o input
                              try:
                                 Quantidade=int(input("Digite a quantidade do item a ser adicionado ao estoque: "))
                              except:
                                 print("\nVocê digitou uma letra. Por favor digite apenas número(s).\n")
                              else:
                                 arquivo.write(f",{Quantidade}") #adicionar a Quantidade no arquivo
                                 break
                  case 3:
                     conteudo=[]
                     with open('cooperativa_log.txt','r+') as arquivo:
                        conteudo= arquivo.read()
                        localizar=input("digite o item que deseja excluir: ")
                        conteudo.index(localizar)
                        
                     

                  case 4:
                     print("\nDesligando sistema. Obrigado por utilizá-lo ^^")
                     break
                                 
         case 4:
            print("\nDesligando sistema. Obrigado por utilizá-lo ^^")
            break

         case _:
            print("\nOpção inválida")