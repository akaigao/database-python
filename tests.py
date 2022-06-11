with open('test.txt', 'r') as file:
    for pos, line in enumerate(file):
        date = line.split(';')
        date[1] = date[1].replace('\n', '')
        print(f'[{pos}] {date[0]:<30} {date[1]:>3} anos')

with open('test.txt', 'r') as file:
    t = file.readlines()
    d = 0
    e = int(input('Digite o índice de acordo com contato '
                  'que você quer excluir: '))

    with open('test.txt', 'w') as file:
        for linex in t:
            if d != e:
                file.write(linex)
            d += 1
        print('Contato excluido com sucesso!')
