def creeazavanzare_carte(id, titlu, gen, pret, tip_reducere):
    """
    Insereaza o carte ce a fost vanduta in baza de date a bibliotecii.
    :param id: string
    :param titlu: string
    :param gen: string
    :param pret: float
    :param tip_reducere: string
    :return: un dictionar ce retine o carte
    """
    dict = [
         id,
         titlu,
         gen,
         pret,
         tip_reducere

    ]
    return dict


def getid(carte):
    """
    Ia id-ul cartii.
    :param carte:dictionar de tipuri de carte
    :return:id-ul cartii
    """
    return carte[0]


def gettitlu(carte):
    """
    Ia titlul cartii.
    :param carte: dictionar de tipuri de carte
    :return: titlul cartii
    """
    return carte[1]


def getgen(carte):
    """
    Ia genul cartii.
    :param carte: dictionar de tipuri de carte
    :return: genul cartii
    """
    return carte[2]


def getpret(carte):
    """
    Ia pretul cartii.
    :param carte: dictionar de tipuri de carte
    :return: pretul cartii
    """
    return carte[3]


def gettip_reducere(carte):
    """
    Ia titlul cartii.
    :param carte: dictionar de tipuri de carte
    :return: titlul cartii
    """
    return carte[4]


def tostring(carte):
    return "id:{}, titlu:{}, gen:{}, pret: {}, tipul de reducere:{}".format(
        getid(carte),
        gettitlu(carte),
        getgen(carte),
        getpret(carte),
        gettip_reducere(carte)
    )

print(list)