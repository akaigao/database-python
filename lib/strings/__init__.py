def title(str):
    print('-'*40)
    print(f'{str:^40}')
    print('-'*40)


def int_validation(op):
    try:
        if op.isdigit() or int(op):
            return True
    except Exception:
        print('\033[0;31mERRO: digite um número inteiro válido.\033[m')
        return False


def str_validation(op):
    if not op.isdigit():
        return True
    else:
        print('\033[0;31mERRO: digite um nome válido.\033[m')
        return False


def option(op):
    if op == 1:
        title('PESSOAS CADASTRADAS')

        with open('contatos.txt', 'r') as file:
            for pos, line in enumerate(file.readlines()):
                line_str = str(line)[0:-1]
                if pos % 2 == 0:
                    print(f'{line_str:<30}', end="")
                else:
                    print(f'{line_str} anos')
            print()

    elif op == 2:
        title('NOVO CADASTRO')

        with open('contatos.txt', 'a+') as file:
            ok = False
            while True:
                name = input('Nome: ').strip()
                ok = str_validation(name)
                if ok:
                    file.write(name)
                    file.write('\n')
                    break

            while True:
                age = input('Idade: ').strip()
                ok = int_validation(age)
                if ok:
                    file.write(age)
                    file.write('\n')
                    break

    elif op == 3:
        title('Saindo do sistema... Até logo!')
        return 3

    else:
        print('\033[0;31mERRO! Digite uma opção válida!\033[m')
