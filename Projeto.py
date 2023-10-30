#criação de um menu para o usuario selecionar qual setor ele quer conferir
def menu_opcao():
    op=int(input(" 1-Para cooperativa\n 2-Para Refeitorio\n 3-Para Agroindustria:\n"))
    return op
match menu_opcao():
    case 1:
        cooperativa()
    case 2:
    
    case 3:
    
    case _:
        print("comando invalido" )


def cooperativa():
    op=int(input(" 1-Ver estoque\n 2-Adicionar item\n 3-Remover item:\n"))
    return op

