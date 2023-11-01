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
         match cooperativa():
            case 1:
                  dados_colunas=[]
                  dados_linhas=[]
                  dados_final=[]
                  with open("cooperativa_log.txt","r") as arquivo: #leitura do arquivo e mostra o estoque detro dele
                     conteudo= arquivo.read()
                     dados_colunas= conteudo.split(";") #separar os dados em colunas
                     for linha in dados_colunas:
                        dados_linhas= linha.split(",") #separar as colunas em linhas
                        dados_final.append(dados_linhas)
                  print(f'\nO estoque contém:')
                  for linha in dados_final:
                     print(linha)
            case 2:
                  matriz=[]
                  texto=""
                  with open("cooperativa_log.txt","a") as arquivo: #leitura do arquivo e mostra o estoque detro dele
                     Item=input("Digite o item a ser adicionado ao estoque: ")
                     arquivo.write(f";{Item}")
                     while True: #validar o input
                        try:
                           Quantidade=int(input("Digite a quantidade do item a ser adicionado ao estoque: "))
                        except:
                           print("\nVocê digitou uma letra. Por favor digite apenas número(s).\n")
                        else:
                           arquivo.write(f",{Quantidade}")
                           break
                     # conteudo= arquivo.read()
                     # for i in range(1):
                     #       for j in range(1):
                     #          addEstoque= input("digite o item a ser adicionado ao estoque: ")
                     #          qtdEstoque= int(input("digite a quantidade do item a ser adicionada ao estoque: "))
                     #          matriz.append(addEstoque)
                     #          matriz.append(qtdEstoque)
                              
      case 4:
         print("\nDesligando sistema. Obrigado por utilizá-lo ^^")
         break

      case _:
         print("\nOpção inválida")