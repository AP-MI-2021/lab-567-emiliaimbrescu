from Domain.librarie import getid, creeazavanzare_carte


def adauga_vanzare_carte(id, titlu, gen, pret, tip_reducere, lista):
    """
    Adauga o noua carte vanduta.
    :param id: string, id-ul cartii nou vandute
    :param titlu: string, titlul cartii noi vandute
    :param gen: string, genul cartii
    :param pret: float, pretul cartii
    :param tip_reducere: string, tipul de reducere pe care il are clientul -> none, silver, gold
    :param lista: lista de carti vandute
    :return: o lista cu cartile vechi si cea nou vanduta
    """
    carte = creeazavanzare_carte(id, titlu, gen, pret, tip_reducere)
    return lista + [carte]


def sterge_carte(id, lista):
    """
    Sterge datele unei carti vandute din lista.
    :param id: id-ul cartii ce trebuie stearsa
    :param lista: lista de carti vandute
    :return: o lista ce contine cartile vechi mai putin pe cea stearsa
    """
    return [carte for carte in lista if getid(carte) != id]


def modifica_carte(id, titlu, gen, pret, tip_reducere, lista):
    """
    Modifica datele unei carti vandute.
    :param id: string, id-ul cartii
    :param titlu: string, titlul cartii
    :param gen: string, genul cartii
    :param pret: float, pretul cartii
    :param tip_reducere: string, tipul de reducere pe care il are clientul -> none, silver, gold
    :param lista: lista de carti vandute
    :return: lista veche cu modificarile efectuate
    """
    listaNoua = []
    for carte in lista:
        if getid(carte) == id:
            carteupdate = creeazavanzare_carte(id, titlu, gen, pret, tip_reducere)
            listaNoua.append(carteupdate)
        else:
            listaNoua.append(carte)
    return listaNoua


def getByID(id, lista):
    """
    Cauta o anumita carte din lista de carti vandute dupa id.
    :param id: id-ul cartii cautate
    :param lista: lista de carti vandute in care se cauta
    :return: datele cartii cautate
    """
    for carte in lista:
        if getid(carte) == id:
            return carte
    return None