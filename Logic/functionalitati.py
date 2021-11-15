from Domain.librarie import creeazavanzare_carte, gettip_reducere, getid, gettitlu, getgen, getpret



def aplicare_discount(lista):
    """
    Aplica un discount de 5% pentru toate reducerile silver și 10% pentru toate reducerile gold.
    :param lista: lista de carti vandute
    :return: noua lista de carti vandute
    """
    listaNoua = []
    for carte in lista:
        if gettip_reducere(carte) == 'silver':
            carteNoua = creeazavanzare_carte(
                getid(carte),
                gettitlu(carte),
                getgen(carte),
                getpret(carte) * 19 / 20,
                gettip_reducere(carte)
            )
            listaNoua.append(carteNoua)
        elif gettip_reducere(carte) == 'gold':
            carteNoua = creeazavanzare_carte(
                getid(carte),
                gettitlu(carte),
                getgen(carte),
                getpret(carte) * 9 / 10,
                gettip_reducere(carte)
            )
            listaNoua.append(carteNoua)
        else:
            listaNoua.append(carte)
    return listaNoua


def modifica_genul(titlu, gen_nou, lista):
    """
    Modifica genul pentru un titlu dat.
    :param lista: lista cartilor vandute
    :param titlu: titlul cartii al carei gen trebuie modificat
    :param gen_nou: noul gen al cartii
    :return: lista cartilor vandute cu genul cartii cautate modificat
    """
    listaNoua = []
    for carte in lista:
        if gettitlu(carte) == titlu:
            carteNoua = creeazavanzare_carte(
                getid(carte),
                gettitlu(carte),
                gen_nou,
                getpret(carte),
                gettip_reducere(carte)
            )
            listaNoua.append(carteNoua)
        else:
            listaNoua.append(carte)
    return listaNoua


def pret_minim(lista):
    """
    Determina prețului minim pentru fiecare gen
    :param lista: lista cartilor vandute
    :return: pretul minim pentru fiecare gen
    """
    rezultat = {}
    for carte in lista:
        gen = getgen(carte)
        pret = getpret(carte)
        if gen in rezultat:
            if pret < rezultat[gen]:
                rezultat[gen] = pret
        else:
            rezultat[gen] = pret
    return rezultat


def ordine_crescatoare(lista):
    """
    Ordoneaza cartile vandute crescător după preț.
    :param lista: lista cartilor vandute
    :return: lista cartilor vandute ordonata crescator dupa pret
    """
    listaNoua = sorted(lista, key=lambda carte: getpret(carte))
    return listaNoua


def titluri_distincte(lista):
    """
    Afișeaza numărul de titluri distincte pentru fiecare gen.
    :param lista: lista cartilor vandute
    :return: numarul de titluri distincte pentru fiecare gen
    """
    rezultat = dict()
    for carte in lista:
        if getgen(carte) not in rezultat:
            rezultat[getgen(carte)] = {gettitlu(carte)}
        else:
            rezultat[getgen(carte)].add(gettitlu(carte))
    return [(gen, len(titluri)) for gen, titluri in rezultat.items()]