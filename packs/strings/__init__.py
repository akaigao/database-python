def menu(op):
    print('-'*40)
    print(f'{"MENU PRINCIPAL":^40}')
    print('-'*40)

    print(' 1 - Ver pessoas cadastradas\n',
          '2 - Cadastrar nova pessoa\n',
          '3 - Sair do sistema')

    print('-'*40)
    return input(op).strip().replace('.', '').replace(',', '')
