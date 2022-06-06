import os
from lib import strings


directory = '/Users/igao/Progamação/'
file = directory + 'projects/1-database-python/contatos.txt'
if os.path.isfile(file):
    pass
else:
    new_file = open('contatos.txt', 'a')
    print('Aquivo contatos.txt criado com sucesso!')


def menu(op):
    strings.title('MENU PRINCIPAL')

    print(' 1 - Ver pessoas cadastradas\n',
          '2 - Cadastrar nova pessoa\n',
          '3 - Sair do sistema')

    print('-'*40)
    answer = input(op).strip().replace('.', '').replace(',', '')
    return strings.validation(answer)


while True:
    option = menu('Sua opção: ')
    if option is False:
        continue
    else:
        option = strings.option(option)
        if option == 3:
            break
