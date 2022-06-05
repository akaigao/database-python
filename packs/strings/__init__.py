def menu(op):
    print('-'*40)
    print(f'{"MENU PRINCIPAL":^40}')
    print('-'*40)

    print(' 1 - Ver pessoas cadastradas\n',
          '2 - Cadastrar nova pessoa\n',
          '3 - Sair do sistema')

    print('-'*40)
    return input(op).strip().replace('.', '').replace(',', '')


def op_validation(op=''):
    while True:
        try:
            op = int(op)
            return option(op)
        except Exception:
            print('ERRO: por favor, digir um número inteiro válido.')
            return op_validation(menu('Sua opção: '))


def option(op):
    if op == 1:
        print('Opção 1')
    elif op == 2:
        print('Opção 2')
    elif op == 3:
        print('Opção 3')
    else:
        print('ERRO! Digite uma opção válida!')
        op_validation(menu('Sua opção: '))
