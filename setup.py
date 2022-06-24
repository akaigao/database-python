from lib import interface

try:
    with open('contatos.txt', 'r') as file:
        pass
except IOError:
    with open('contatos.txt', 'a') as file:
        print(f'Arquivo {file} criado com sucesso!')


while True:
    option = interface.menu('Sua opção: ')
    try:
        interface.option(int(option))
        if int(option) == 6:
            break
    except Exception:
        continue
