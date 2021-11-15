from Domain.librarie import tostring
from Logic.CRUD import adauga_vanzare_carte, sterge_carte, modifica_carte
from Logic.functionalitati import aplicare_discount, ordine_crescatoare, pret_minim, modifica_genul, titluri_distincte


def printMenu():
    print("1. Adaugati o carte vanduta in lista.")
    print("2. Stergeti o carte din lista.")
    print("3. Modificati o carte din lista.")
    print("4. Aplica discount-urile.")
    print("5. Modificati genul unei carti dupa titlul dorit.")
    print("6. Afisati pretul minim pentru fiecare gen.")
    print("7. Afisati in ordine crescatoare dupa pret a listei.")
    print("8. Afisati numarul de titluri distincte pentru fiecare gen.")
    print("U. Undo")
    print("R. Redo")
    print("A. Arata toate cartile.")
    print("x. Iesire.")


def uiAdauga_o_carte(lista, undo_list, redo_list):
    try:
        id = input("Insereaza id-ul cartii pe care doresti sa o adaugi:")
        titlu = input("Insereaza titlul cartii pe care doresti sa o adaugi:")
        gen = input("Insereaza genul cartii pe care doresti sa o adaugi:")
        pret = float(input("Insereaza pretul cartii pe care doresti sa o adaugi:"))
        tip_reducere = input("Insereaza tipul de reducere pe care cumparatorul cartii il are:")
        rezultat = adauga_vanzare_carte(id, titlu, gen, pret, tip_reducere, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiSterge_o_carte(lista, undo_list, redo_list):
    try:
        id = input("Inserati id-ul cartii pe care doriti sa o stergeti:")
        rezultat = sterge_carte(id, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiModifica_o_carte(lista, undo_list, redo_list):
    try:
        id = input("Insereaza id-ul cartii pe care doresti sa o modifici:")
        titlu = input("Insereaza noul titlu:")
        gen = input("Insereaza genul cartii noi:")
        pret = float(input("Insereaza noul pretul:"))
        tip_reducere = input("Insereaza tipul de reducere pe care cumparatorul cartii il are:")
        rezultat = modifica_carte(id, titlu, gen, pret, tip_reducere, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def showAll(lista):
    for carte in lista:
        print(tostring(carte))


def uiAplica_discount(lista, undo_list, redo_list):
    rezultat = aplicare_discount(lista)
    undo_list.append(lista)
    redo_list.clear()
    return rezultat


def uiPret_minim(lista):
    rezultat = pret_minim(lista)
    for gen in rezultat:
        print("Pretul minim pentru genul {} este {}".format(gen, rezultat[gen]))


def uiOrdine_crescatoare(lista, undo_list, redo_list):
    listaNoua = ordine_crescatoare(lista)
    undo_list.append(lista)
    redo_list.clear()
    return listaNoua


def uiTitluri_distincte(lista):
    perechi = titluri_distincte(lista)
    for gen, nr_titluri in perechi:
        print(f"{gen}: {nr_titluri}")


def uiModifica_genul_cartii(lista, undo_list, redo_list):
    titlu = input("Introduceti titlul cartii al carei gen doriti sa il modificati: ")
    gen_nou = input("Introduceti noul gen: ")
    rezultat = modifica_genul(titlu, gen_nou, lista)
    undo_list.append(lista)
    redo_list.clear()
    return rezultat


def runMenu(lista):
    undo_list = []
    redo_list = []
    while True:
        printMenu()
        optiune = input("Alegeti o optiune:")
        if optiune == '1':
            lista = uiAdauga_o_carte(lista, undo_list, redo_list)
        elif optiune == '2':
            lista = uiSterge_o_carte(lista, undo_list, redo_list)
        elif optiune == '3':
            lista = uiModifica_o_carte(lista, undo_list, redo_list)
        elif optiune == '4':
            lista = uiAplica_discount(lista, undo_list, redo_list)
        elif optiune == '5':
            lista = uiModifica_genul_cartii(lista, undo_list, redo_list)
        elif optiune == '6':
            uiPret_minim(lista)
        elif optiune == '7':
            lista = uiOrdine_crescatoare(lista, undo_list, redo_list)
        elif optiune == '8':
            uiTitluri_distincte(lista)
        elif optiune == "U":
            if len(undo_list) > 0:
                redo_list.append(lista)
                lista = undo_list.pop()
            else:
                print("Nu se poate face undo!")
        elif optiune == "R":
            if len(redo_list) > 0:
                undo_list.append(lista)
                lista = redo_list.pop()
            else:
                print("Nu se poate face redo!")
        elif optiune == 'A':
            showAll(lista)
        elif optiune == 'x':
            break
        else:
            print("Optiunea aleasa nu este din meniu. Alege alta optiune:")
