from Logic.CRUD import adauga_vanzare_carte
from Tests.testAll import run_all_tests
from UserInterface.console import runMenu


def main():
    run_all_tests()
    lista = []
    lista = adauga_vanzare_carte('1', 'Spune-mi ce visezi', 'politist', 44, 'none', lista)
    lista = adauga_vanzare_carte('2', 'Me before you', 'dragoste', 35.60, 'silver', lista)
    runMenu(lista)


main()
