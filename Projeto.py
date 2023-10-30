#criação de um menu para o usuario selecionar qual setor ele quer conferir
def menu_opcao():
  print(" Bem vindo(a) ao IF Administra! Qual estoque você deseja entrar?\n 1-Cooperativa\n 2-Refeitorio\n 3-Agroindustria:\n")
  while True: #validar a opção do input
    try:
      op = int(input("Digite a opção desejada: "))
    except:
      print("Você digitou uma letra. Por favor digite apenas número.")
    else:
      return op

def cooperativa(): #menu de opções da coooperativa
    op=int(input(" \nCooperativa! O que você deseja fazer?\n 1-Ver estoque\n 2-Adicionar item\n 3-Remover item\n 4-Voltar ao menu principal:\n"))
    while True:
     try:
        op = int(input("Digite a opção desejada: "))
     except:
        print("Você digitou uma letra. Por favor digite apenas número.")
     else:
        return op

def refeitorio(): #menu de opções do refeitorio
    op=int(input(" \nRefeitório! O que você deseja fazer?\n 1-Ver estoque\n 2-Adicionar item\n 3-Remover item\n 4-Voltar ao menu principal:\n"))
    while True:
     try:
        op = int(input("Digite a opção desejada: "))
     except:
        print("Você digitou uma letra. Por favor digite apenas número.")
     else:
        return op

def agroindustria(): #menu de opções do agroindustria
    op=int(input(" \nAgroindústria! O que você deseja fazer?\n 1-Ver estoque\n 2-Adicionar item\n 3-Remover item\n 4-Voltar ao menu principal:\n"))
    while True:
     try:
        op = int(input("Digite a opção desejada: "))
     except:
        print("Você digitou uma letra. Por favor digite apenas número.")
     else:
        return op

#Codigo
match menu_opcao():
    case 1:
       match cooperativa():
           case 1:
                with open("cooperativa.txt","r") as arquivo: #leitura do arquivo e mostra o estoque detro dele
                    conteudo= arquivo.read()
                print(conteudo)
           case 2:
                matriz=[]
                with open("cooperativa.txt","r") as arquivo: #leitura do arquivo e mostra o estoque detro dele
                    conteudo= arquivo.read()
                    for linha in matriz:
                        matriz.append(input(""))
                        for coluna in matriz:
                            


    case 2:
        refeitorio()
    case _:
        print("comando invalido\n" )