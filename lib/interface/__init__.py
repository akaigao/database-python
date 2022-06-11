from lib import validation


def title(str='TÍTULO'):
    print('-'*42)
    print(f'{str:^42}')
    print('-'*42)


def menu(op=0):
    title('MENU PRINCIPAL')

    print(' 1 - Ver pessoas cadastradas\n',
          '2 - Cadastrar nova pessoa\n',
          '3 - Sair do sistema')

    print('-'*40)
    return validation.read_int(op)


def option(op=0):
    if op == 1:
        title('PESSOAS CADASTRADAS')

        with open('contatos.txt', 'r') as file:
            for line in file:
                date = line.split(';')
                date[1] = date[1].replace('\n', '')
                print(f'{date[0]:<30} {date[1]:>3} anos')

    elif op == 2:
        title('NOVO CADASTRO')

        with open('contatos.txt', 'a+') as file:
            name = validation.read_str('Nome: ')
            age = validation.read_int('Idade: ')
            file.write(f'{name};{age}\n')

    elif op == 3:
        title('Saindo do sistema... Até logo!')
        return 3

    else:
        print('\033[0;31mERRO! Digite uma opção válida!\033[m')
