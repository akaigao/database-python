from packs import strings


def op_validation(op=''):
    while True:
        try:
            op = int(op)
            return option(op)
        except Exception:
            print('ERRO: por favor, digir um número inteiro válido.')
            strings.menu('Sua opção: ')


def option(op):
    if op == 1:
        print(type(op))
    elif op == 2:
        pass
    elif op == 3:
        pass
    else:
        print(type(op))


tes = strings.menu('Sua opção: ')
op_validation(tes)
