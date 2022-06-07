from lib import strings

try:
    with open('contatos.txt', 'r') as file:
        pass
except IOError:
    with open('contatos.txt', 'a') as file:
        print('Arquvio contatos.txt criado com sucesso!')


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
