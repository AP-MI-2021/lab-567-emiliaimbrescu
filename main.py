from Logic.CRUD import adauga_vanzare_carte
from Tests.testAll import run_all_tests
from UserInterface.console import runMenu
from UserInterface.new_console import run_console


def alege_meniul():
    print('1. Meniul clasic')
    print('2. Meniul nou')
    print('EXIT. Iesire')

def main():
    run_all_tests()
    lista = []
    lista = adauga_vanzare_carte('1', 'Spune-mi ce visezi', 'politist', 44, 'none', lista)
    lista = adauga_vanzare_carte('2', 'Me before you', 'dragoste', 35.60, 'silver', lista)
    while True:
        alege_meniul()
        optiune = input('Alegeti optiunea: ')
        if optiune == '1':
            runMenu(lista)
        elif optiune == '2':
            run_console(lista)
        elif optiune == 'EXIT':
            break
        else:
            print('Optiune invalida!')


main()
