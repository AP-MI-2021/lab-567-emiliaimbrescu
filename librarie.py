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
    return{
        'id': id,
        'titlu': titlu,
        'gen': gen,
        'pret': pret,
        'tip_reducere': tip_reducere

    }


def getid(carte):
    """
    Ia id-ul cartii.
    :param carte:dictionar de tipuri de carte
    :return:id-ul prajiturii
    """
    return carte['id']


def gettitlu(carte):
    """
    Ia titlul cartii.
    :param carte: dictionar de tipuri de carte
    :return: titlul cartii
    """
    return carte['titlu']


def getgen(carte):
    """
    Ia genul cartii.
    :param carte: dictionar de tipuri de carte
    :return: genul cartii
    """
    return carte['gen']


def getpret(carte):
    """
    Ia pretul cartii.
    :param carte: dictionar de tipuri de carte
    :return: pretul cartii
    """
    return carte['pret']


def gettip_reducere(carte):
    """
    Ia titlul cartii.
    :param carte: dictionar de tipuri de carte
    :return: titlul cartii
    """
    return carte['tip_reducere']


def tostring(carte):
    return "id:{}, titlu:{}, gen:{}, pret: {}, tipul de reducere:{}".format(
        getid(carte),
        gettitlu(carte),
        getgen(carte),
        getpret(carte),
        gettip_reducere(carte)
    )
