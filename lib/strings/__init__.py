def title(str):
    print('-'*40)
    print(f'{str:^40}')
    print('-'*40)


def validation(op):
    while True:
        try:
            return int(op)
        except Exception:
            print('\033[0;31mERRO: digite um número inteiro válido.\033[m')
            return False


def option(op=0):
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

        file = open('contatos.txt', 'a+')
        datashet = []

        datashet.append(input('Nome: '))
        datashet.append(input('Idade: '))

        for line in datashet:
            file.write(line)
            file.write("\n")

        datashet.clear()
        file.close()

    elif op == 3:
        title('Saindo do sistema... Até logo!')
        return 3

    else:
        print('\033[0;31mERRO! Digite uma opção válida!\033[m')
