from lib import validation


def read_file(show_index=False):
    with open('contatos.txt', 'r') as file:
        for pos, line in enumerate(file):
            date = line.split(';')
            date[1] = date[1].replace('\n', '')
            if show_index:
                print(f'[{pos}] {date[0]:<30} {date[1]:>3} anos')
            else:
                print(f'{date[0]:<30} {date[1]:>3} anos')


def write_file():
    with open('contatos.txt', 'a+') as file:
        name = validation.read_str('Nome: ')
        age = validation.read_int('Idade: ')
        file.write(f'{name};{age}\n')


def del_file():
    read_file(show_index=True)

    with open('contatos.txt', 'r') as fl1:
        lines = fl1.readlines()

        pointer = 0
        index = validation.read_int(
            'Digite o índice de acordo '
            'com o cadastro que você quer EXCLUIR: ')

        with open('contatos.txt', 'w') as fl2:
            for line in lines:
                if pointer != index:
                    fl2.write(line)
                pointer += 1
            print('Cadastro excluído com sucesso!')


def change_file():
    read_file(show_index=True)

    with open('contatos.txt', 'r') as fl1:
        lines = fl1.readlines()

        pointer = 0
        index = validation.read_int(
            'Digire o índice de acordo '
            'com o cadastro que você quer ALTERAR: ')

        with open('contatos.txt', 'w') as fl2:
            for line in lines:
                if pointer != index:
                    fl2.writelines(line)
                elif pointer == index:
                    name = validation.read_str('Novo Nome: ')
                    age = validation.read_int('Nova Idade: ')
                    fl2.write(f'{name};{age}\n')
                pointer += 1
            print('Cadastro alterado com sucesso!')
