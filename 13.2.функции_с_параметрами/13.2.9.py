def print_fio(name, surname, patronymic):
    print(f"{surname[0]}{name[0]}{patronymic[0]}".upper())


name = input()
surname = input()
patronymic = input()
print_fio(name, surname, patronymic)