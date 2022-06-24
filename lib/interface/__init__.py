from lib import file, validation


def title(str='TÍTULO'):
    print('-'*42)
    print(f'{str:^42}')
    print('-'*42)


def menu(op=0):
    title('MENU PRINCIPAL')

    print(' 1 - Ver pessoas cadastradas\n',
          '2 - Cadastrar nova pessoa\n',
          '3 - Procurar cadastro\n',
          '4 - Alterar um cadastro\n',
          '5 - Excluir um cadastro\n',
          '6 - Sair do Sistema')

    print('-'*40)
    return validation.read_int(op)


def option(op=0):
    if op == 1:
        title('PESSOAS CADASTRADAS')

        file.read_file(show_index=False)

    elif op == 2:
        title('NOVO CADASTRO')

        file.write_file()

    elif op == 3:
        title('PROCURAR CADASTRO')

        file.find_file()

    elif op == 4:
        title('ALTERAR CADASTRO')

        file.change_file()

    elif op == 5:
        title('EXCLUSSÃO DE CADASTRO')

        file.del_file()

    elif op == 6:
        title('Saindo do sistema... Até logo!')
        return 5

    else:
        print('\033[0;31mERRO! Digite uma opção válida!\033[m')
