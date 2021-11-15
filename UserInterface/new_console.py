from Domain.librarie import getid, tostring
from Logic.CRUD import adauga_vanzare_carte, getByID


def print_help():
    print("Comenzi disponibile: ")
    print("Ajutor")
    print("Adauga carte vanduta: adauga, id, titlu, gen, pret, reducere")
    print("Sterge carte vanduta: sterge, id")
    print("Afisare")
    print("Stop")
    print("Parametrii trebuie separati prin virgula.")
    print("Comenzile trebuie separate prin ;")


def adauga(lista, parametrii):
    id = str(parametrii[1])
    titlu = str(parametrii[2])
    gen = str(parametrii[3])
    pret = float(parametrii[4])
    reducere = str(parametrii[5])
    lista = adauga_vanzare_carte(id, titlu, gen, pret, reducere, lista)
    return lista


def sterge(lista, parametrii):

    if getByID(parametrii[1], lista) is None:
        raise ValueError("Nu exista carte cu Id-ul dat")
    return [carte for carte in lista if getid(carte) != parametrii[1]]


def showall(lista):
    for carte in lista:
        print(tostring(carte))


def run_console(lista):
    contor = True
    while contor:
        comenzi = input("Introduceti comenzile: ")
        functii = comenzi.split(";")
        for functie in functii:
            parametrii = functie.split(",")
            if parametrii[0] == "Ajutor":
                print_help()
            elif parametrii[0] == "Adauga":
                lista = adauga(lista, parametrii)
            elif parametrii[0] == "Sterge":
                lista = sterge(lista, parametrii)
            elif parametrii[0] == "Afisare":
                print("Lista de vanzari este: ")
                showall(lista)
            elif parametrii[0] == "Stop":
                contor = False