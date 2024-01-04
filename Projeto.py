def menu_opcao():  # criação de um menu para o usuario selecionar qual setor ele quer conferir o estoque
    print("\nBem vindo(a) ao IF Administra! Qual estoque você deseja entrar?\n 1-Cooperativa\n 2-Refeitorio\n 3-Agroindustria\n 4-Sair do programa")
    while True:  # para deixar o while infinito
        try:  # faz com que o Python tente executar o código abaixo e caso não consiga irá entrar no except
            op = int(input("\nDigite a opção desejada: "))
        except:  # tratrando o erro. Irá aparecer a mensagem que está no print ao invés de um erro em inglês e que pode não ser intuitivo
            print("\nVocê digitou uma letra ou um caracter inválido. Por favor digite apenas os números que estão no menu de opções.")
        else:  # aqui além de sair do while, irá retornar o valor da variável de op. Só irá passar por aqui caso não entre no except
            return op


def cooperativa():  # menu de opções da coooperativa
    print(" \nCooperativa! O que você deseja fazer?\n 1-Ver estoque\n 2-Adicionar item\n 3-Remover item\n 4-Voltar ao menu principal")
    while True:  # para deixar o while infinito
        try:  # faz com que o Python tente executar o código abaixo e caso não consiga irá entrar no except
            op = int(input("\nDigite a opção desejada: "))
        except:  # tratrando o erro. Irá aparecer a mensagem que está no print ao invés de um erro em inglês e que pode não ser intuitivo
            print("\nVocê digitou uma letra. Por favor digite apenas número.")
        else:  # aqui além de sair do while, irá retornar o valor da variável de op. Só irá passar por aqui caso não entre no except
            return op


def refeitorio():  # menu de opções do refeitorio
    print(" \nRefeitório! O que você deseja fazer?\n 1-Ver estoque\n 2-Adicionar item\n 3-Remover item\n 4-Voltar ao menu principal")
    while True:  # para deixar o while infinito
        try:  # faz com que o Python tente executar o código abaixo e caso não consiga irá entrar no except
            op = int(input("\nDigite a opção desejada: "))
        except:  # tratrando o erro. Irá aparecer a mensagem que está no print ao invés de um erro em inglês e que pode não ser intuitivo
            print("\nVocê digitou uma letra. Por favor digite apenas número.")
        else:  # aqui além de sair do while, irá retornar o valor da variável de op. Só irá passar por aqui caso não entre no except
            return op


def agroindustria():  # menu de opções do agroindustria
    print(" \nAgroindústria! O que você deseja fazer?\n 1-Ver estoque\n 2-Adicionar item\n 3-Remover item\n 4-Voltar ao menu principal")
    while True:  # para deixar o while infinito
        try:  # faz com que o Python tente executar o código abaixo e caso não consiga irá entrar no except
            op = int(input("\nDigite a opção desejada: "))
        except:  # tratrando o erro. Irá aparecer a mensagem que está no print ao invés de um erro em inglês e que pode não ser intuitivo
            print("\nVocê digitou uma letra. Por favor digite apenas número.")
        else:  # aqui além de sair do while, irá retornar o valor da variável de op. Só irá passar por aqui caso não entre no except
            return op

# Codigo


while True:  # deixa o programa rodando infinitamente, ao menos que escolha a opção para sair do programa
    match menu_opcao():  # no match já inserimos a função
        case 1:
            while True:  # faz com que o menu da cooperativa rode infinitamente ao menos que escolha a opção para sair do programa
                match cooperativa():  # no match já inserimos a função
                    case 1:
                        print("\nO estoque da cooperativa possui: ")
                        # leitura do arquivo e mostra o estoque detro dele
                        with open("cooperativa_log.txt", "r") as arquivo:
                            conteudo = arquivo.read()
                            # remove os cochetes de abertura e fechamento do arquivo.
                            conteudo = conteudo[1:-1]
                            # divide o texto em pares separados por ,
                            pares = conteudo.split(", ")
                            for par in pares:
                                print(par)
                    case 2:
                        estoque = {}

                        while True:
                            item = input(
                                "\nDigite o item a ser adicionado ao estoque: ")
                            if item.isalpha() == True:  # verifica se o usuario digitou somente string alfabetica.
                                break
                            else:
                                print("\nDigite apenas letras.")

                        while True:
                            try:  # faz com que o Python tente executar o código abaixo e caso não consiga irá entrar no except
                                quantidade = int(
                                    input("\nDigite a quantidade desse item: "))
                            except:  # tratrando o erro. Irá aparecer a mensagem que está no print ao invés de um erro em inglês e que pode não ser intuitivo
                                print(
                                    "\nVocê digitou uma letra. Por favor digite apenas número.")
                            else:  # aqui além de sair do while, irá retornar o valor da variável de op. Só irá passar por aqui caso não entre no except
                                break

                        # convertendo arquivo em dicionario \/
                        # leitura do arquivo e mostra o estoque detro dele
                        with open("cooperativa_log.txt", "r") as arquivo:
                            conteudo = arquivo.read()
                            # remove os cochetes de abertura e fechamento do arquivo.
                            conteudo = conteudo[1:-1]
                            # divide o texto em pares separados por ,
                            pares = conteudo.split(", ")
                            for par in pares:
                                # separa a string do valor
                                chave, valor = par.split(": ")
                                # adiciona a chave e o valor ao dicionario removendo as aspas simples e só aceitando valores inteiros
                                estoque[chave.strip("'")] = int(valor)
                        estoque[item] = quantidade
                        # convertendo dicionario em string e atualizando arquivo de texto.
                        converter_para_string = str(estoque)
                        with open('cooperativa_log.txt', 'w') as arquivo:
                            arquivo.write(converter_para_string)
                        print(
                            f"\nO seu item {item} foi adicionado com a quantidade {quantidade} no sistema!")
                    case 3:
                        estoque = {}

                        while True:
                            deletar = input(
                                "\nDigite o item a ser excluido do estoque: ")
                            # verifica se o usuario digitou somente string alfabetica.
                            if deletar.isalpha() == True:
                                break
                            else:
                                print("\nDigite apenas letras.")

                        with open('cooperativa_log.txt', 'r') as arquivo:
                            conteudo = arquivo.read()
                        # removendo cochete do inicio e do final
                        conteudo = conteudo[1:-1]
                        # dividindo o conteudo em pares separados por ,
                        pares = conteudo.split(", ")
                        for par in pares:
                            # separa a string do valor
                            chave, valor = par.split(": ")
                            # adiciona a chave e o valor ao dicionario removendo a aspas simples e so aceitando valores inteiros
                            estoque[chave.strip("'")] = int(valor)
                        consulta = deletar in estoque

                        if consulta == True:  # só irá entrar aqui se o o item inserido na variável deletar estiver no estoque
                            print("\nO item existe no estoque!")
                            del estoque[deletar]
                            # convertendo dicionario em string para salvar em arquivo
                            convetido = str(estoque)
                            with open('cooperativa_log.txt', 'w') as arquivo:
                                arquivo.write(convetido)
                            # o arquivo fica salvo com os cochetes do dicionario, arrumar uma forma para remover isso ou muda o codigo de matriz para dicionario
                            print(
                                f'\nO item {deletar} foi deletado com sucesso!')

                        else:
                            print("\nO item não existe no estoque!")

                    case 4:
                        print("\nVoltando ao menu principal ^^")
                        break
        case 2:
            while True:  # faz com que o menu do refeitório rode infinitamente ao menos que escolha a opção para sair do programa
                match refeitorio():  # no match já inserimos a função
                    case 1:
                        print("\nO estoque do refeitorio possui: ")
                        # leitura do arquivo e mostra o estoque detro dele
                        with open("refeitorio_log.txt", "r") as arquivo:
                            conteudo = arquivo.read()
                            # remove os cochetes de abertura e fechamento do arquivo.
                            conteudo = conteudo[1:-1]
                            # divide o texto em pares separados por ,
                            pares = conteudo.split(", ")
                            for par in pares:
                                print(par)
                    case 2:
                        estoque = {}

                        while True:
                            item = input(
                                "\nDigite o item a ser adicionado ao estoque: ")
                            if item.isalpha() == True:  # verifica se o usuario digitou somente string alfabetica.
                                break
                            else:
                                print("\nDigite apenas letras.")

                        while True:
                            try:  # faz com que o Python tente executar o código abaixo e caso não consiga irá entrar no except
                                quantidade = int(
                                    input("\nDigite a quantidade desse item: "))
                            except:  # tratrando o erro. Irá aparecer a mensagem que está no print ao invés de um erro em inglês e que pode não ser intuitivo
                                print(
                                    "\nVocê digitou uma letra. Por favor digite apenas número.")
                            else:  # aqui além de sair do while, irá retornar o valor da variável de op. Só irá passar por aqui caso não entre no except
                                break

                        # convertendo arquivo em dicionario \/
                        # leitura do arquivo e mostra o estoque detro dele
                        with open("refeitorio_log.txt", "r") as arquivo:
                            conteudo = arquivo.read()
                            # remove os cochetes de abertura e fechamento do arquivo.
                            conteudo = conteudo[1:-1]
                            # divide o texto em pares separados por ,
                            pares = conteudo.split(", ")
                            for par in pares:
                                # separa a string do valor
                                chave, valor = par.split(": ")
                                # adiciona a chave e o valor ao dicionario removendo a aspas simples e so aceitando valores inteiros
                                estoque[chave.strip("'")] = int(valor)
                        estoque[item] = quantidade
                        # convertendo dicionario em string e atualizando arquivo de texto.
                        converter_para_string = str(estoque)
                        with open('refeitorio_log.txt', 'w') as arquivo:
                            arquivo.write(converter_para_string)
                        print(
                            f"\nO seu item {item} foi adicionado com a quantidade {quantidade} no sistema!")
                    case 3:
                        estoque = {}

                        while True:
                            deletar = input(
                                "\nDigite o item a ser excluido do estoque: ")
                            # verifica se o usuario digitou somente string alfabetica.
                            if deletar.isalpha() == True:
                                break
                            else:
                                print("\nDigite apenas letras.")

                        with open('refeitorio_log.txt', 'r') as arquivo:
                            conteudo = arquivo.read()
                        # removendo cochete do inicio e do final
                        conteudo = conteudo[1:-1]
                        # dividindo o conteudo em pares separados por ,
                        pares = conteudo.split(", ")
                        for par in pares:
                            # separa a string do valor
                            chave, valor = par.split(": ")
                            # adiciona a chave e o valor ao dicionario removendo a aspas simples e so aceitando valores inteiros
                            estoque[chave.strip("'")] = int(valor)
                        consulta = deletar in estoque

                        if consulta == True:  # só irá entrar aqui se o o item inserido na variável deletar estiver no estoque
                            print("\nO item existe no estoque!")
                            del estoque[deletar]
                            # convertendo dicionario em string para salvar em arquivo
                            convetido = str(estoque)
                            with open('refeitorio_log.txt', 'w') as arquivo:
                                arquivo.write(convetido)
                            # o arquivo fica salvo com os cochetes do dicionario, arrumar uma forma para remover isso ou muda o codigo de matriz para dicionario
                            print(
                                f'\nO item {deletar} foi deletado com sucesso!')

                        else:
                            print("\nO item não existe no estoque!")

                    case 4:
                        print("\nVoltando ao menu principal ^^")
                        break
        case 3:
            while True:  # faz com que o menu do agroindústria rode infinitamente ao menos que escolha a opção para sair do programa
                match agroindustria():  # no match já inserimos a função
                    case 1:
                        print("\nO estoque do agroindustria possui: ")
                        # leitura do arquivo e mostra o estoque detro dele
                        with open("agroindustria_log.txt", "r") as arquivo:
                            conteudo = arquivo.read()
                            # remove os cochetes de abertura e fechamento do arquivo.
                            conteudo = conteudo[1:-1]
                            # divide o texto em pares separados por ,
                            pares = conteudo.split(", ")
                            for par in pares:
                                print(par)
                    case 2:
                        estoque = {}

                        while True:
                            item = input(
                                "\nDigite o item a ser adicionado ao estoque: ")
                            if item.isalpha() == True:  # verifica se o usuario digitou somente string alfabetica.
                                break
                            else:
                                print("\nDigite apenas letras.")

                        while True:
                            try:  # faz com que o Python tente executar o código abaixo e caso não consiga irá entrar no except
                                quantidade = int(
                                    input("\nDigite a quantidade desse item: "))
                            except:  # tratrando o erro. Irá aparecer a mensagem que está no print ao invés de um erro em inglês e que pode não ser intuitivo
                                print(
                                    "\nVocê digitou uma letra. Por favor digite apenas número.")
                            else:  # aqui além de sair do while, irá retornar o valor da variável de op. Só irá passar por aqui caso não entre no except
                                break

                        # convertendo arquivo em dicionario \/
                        # leitura do arquivo e mostra o estoque detro dele
                        with open("agroindustria_log.txt", "r") as arquivo:
                            conteudo = arquivo.read()
                            # remove os cochetes de abertura e fechamento do arquivo.
                            conteudo = conteudo[1:-1]
                            # divide o texto em pares separados por ,
                            pares = conteudo.split(", ")
                            for par in pares:
                                # separa a string do valor
                                chave, valor = par.split(": ")
                                # adiciona a chave e o valor ao dicionario removendo a aspas simples e so aceitando valores inteiros
                                estoque[chave.strip("'")] = int(valor)
                        estoque[item] = quantidade
                        # convertendo dicionario em string e atualizando arquivo de texto.
                        converter_para_string = str(estoque)
                        with open('agroindustria_log.txt', 'w') as arquivo:
                            arquivo.write(converter_para_string)
                        print(
                            f"\nO seu item {item} foi adicionado com a quantidade {quantidade} no sistema!")
                    case 3:
                        estoque = {}

                        while True:
                            deletar = input(
                                "\nDigite o item a ser excluido do estoque: ")
                            # verifica se o usuario digitou somente string alfabetica.
                            if deletar.isalpha() == True:
                                break
                            else:
                                print("\nDigite apenas letras.")

                        with open('agroindustria_log.txt', 'r') as arquivo:
                            conteudo = arquivo.read()
                        # removendo cochete do inicio e do final
                        conteudo = conteudo[1:-1]
                        # dividindo o conteudo em pares separados por ,
                        pares = conteudo.split(", ")
                        for par in pares:
                            # separa a string do valor
                            chave, valor = par.split(": ")
                            # adiciona a chave e o valor ao dicionario removendo a aspas simples e so aceitando valores inteiros
                            estoque[chave.strip("'")] = int(valor)
                        consulta = deletar in estoque

                        if consulta == True:  # só irá entrar aqui se o o item inserido na variável deletar estiver no estoque
                            print("\nO item existe no estoque!")
                            del estoque[deletar]
                            # convertendo dicionario em string para salvar em arquivo
                            convetido = str(estoque)
                            with open('agroindustria_log.txt', 'w') as arquivo:
                                arquivo.write(convetido)
                            # o arquivo fica salvo com os cochetes do dicionario, arrumar uma forma para remover isso ou muda o codigo de matriz para dicionario
                            print(
                                f'\nO item {deletar} foi deletado com sucesso!')

                        else:
                            print("\nO item não existe no estoque!")

                    case 4:
                        print("\nVoltando ao menu principal ^^")
                        break
        case 4:
            print("\nDesligando sistema. Obrigado por utilizá-lo ^^")
            break
        case _:
            print("\nPor favor, selecione uma das opções do menu: ")
