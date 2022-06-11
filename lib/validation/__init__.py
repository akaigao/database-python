def read_int(inpt):
    inpt = input(inpt).strip()
    while True:
        try:
            if inpt.isdigit() or int(inpt):
                return int(inpt)
        except Exception:
            print('\033[0;31mERRO: digite um número inteiro válido.\033[m')
            inpt = input('Sua opção: ').strip()


def read_str(inpt):
    inpt = input(inpt).strip()
    while True:
        if not inpt == "":
            return inpt
        else:
            print('\033[0;31mERRO: NOME não pode ficar em branco.\033[m')
            inpt = input('Nome: ').strip()
