'''with open('contatos.txt', 'r') as file:
    for pos, line in enumerate(file.readlines()):
        value = line.split()
        if pos % 2 == 1:
            print(*value, 'anos', end="\n")
        else:
            print(tabulate(value))
    print()'''

with open('contatos.txt', 'r') as file:
    for pos, line in enumerate(file.readlines()):
        ln_str = str(line)[0:-1]
        if pos % 2 == 0:
            print(f'{ln_str:<40}', end=" ")
        else:
            print(f'{ln_str} anos')
    print()
