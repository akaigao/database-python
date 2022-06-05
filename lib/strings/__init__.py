def op_validation(op=''):
    while True:
        try:
            op = int(op)
            return option(op)
        except Exception:
            print('\033[0;31mERRO: digite um número inteiro válido.\033[m')
            return False


def option(op):
    if op == 1:
        print('Opção 1')
        # op_validation(menu('Sua opção: '))
    elif op == 2:
        print('Opção 2')
        # op_validation(menu('Sua opção: '))
    elif op == 3:
        print('-'*40)
        print(f'{"Saindo do sistema... Até logo!":^40}')
        print('-'*40)
    else:
        print('\033[0;31mERRO! Digite uma opção válida!\033[m')
        # op_validation(menu('Sua opção: '))
