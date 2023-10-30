#criação de um menu para o usuario selecionar qual setor ele quer conferir
def menu_opcao():
    op=int(input(" 1-Para cooperativa\n 2-Para Refeitorio\n 3-Para Agroindustria:\n"))
    if (op!=int):
        print("Digite um número valido!")
    return op

def cooperativa(): #menu de opções da coooperativa
    op=int(input(" 1-Ver estoque\n 2-Adicionar item\n 3-Remover item:\n"))
    if (op!=int):
        print("Digite um número valido!")
    return op

match menu_opcao():
    case 1:
        cooperativa()
    case _:
        print("comando invalido\n" )

menu_opcao()