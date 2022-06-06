for pos, line in enumerate(file.readlines()):
            value = line.split()
            if pos % 2 == 1:
                print(f"\t\t{value} anos\n", end="")
            else:
                print(value, end="")
        print()