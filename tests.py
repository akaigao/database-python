new_aqr = open('contatos.txt', "a")

aqr = open('contatos.txt', 'r')

for item in aqr.readlines():
    print(item, end="")
print()
