from Domain.librarie import tostring
from Logic.CRUD import adauga_vanzare_carte, sterge_carte, modifica_carte


def uiAdauga_o_carte(lista):
    id = input("Insereaza id-ul cartii pe care doresti sa o adaugi:")
    titlu = input("Insereaza titlul cartii pe care doresti sa o adaugi:")
    gen = input("Insereaza genul cartii pe care doresti sa o adaugi:")
    pret = float(input("Insereaza pretul cartii pe care doresti sa o adaugi:"))
    tip_reducere = input("Insereaza tipul de reducere pe care cumparatorul cartii il are:")
    return adauga_vanzare_carte(id, titlu, gen, pret, tip_reducere, lista)


def uiSterge_o_carte(lista):
    id = input("Inserati id-ul cartii pe care doriti sa o stergeti:")
    return sterge_carte(id, lista)


def uiModifica_o_carte(lista):
    id = input("Insereaza id-ul cartii pe care doresti sa o modifici:")
    titlu = input("Insereaza noul titlu:")
    gen = input("Insereaza genul cartii noi:")
    pret = float(input("Insereaza noul pretul:"))
    tip_reducere = input("Insereaza tipul de reducere pe care cumparatorul cartii il are:")
    return modifica_carte(id, titlu, gen, pret, tip_reducere, lista)


def showAll(lista):
    for carte in lista:
        print(tostring(carte))


def printMenu():
    print("1. Adaugati o carte vanduta in lista.")
    print("2. Stergeti o carte din lista.")
    print("3. Modificati o carte din lista.")
    print("A. Arata toate cartile.")
    print("x. Iesire.")

def runMenu(lista):
    while True:
        printMenu()
        optiune = input( "Alegeti o optiune:")
        if optiune == '1':
            lista = uiAdauga_o_carte(lista)
        elif optiune == '2':
            lista = uiSterge_o_carte(lista)
        elif optiune == '3':
            lista = uiModifica_o_carte(lista)
        elif optiune == 'A':
            showAll(lista)
        elif optiune == 'x':
            break
        else:
            print("Optiunea aleasa nu este din meniu. Alege alta optiune:")
