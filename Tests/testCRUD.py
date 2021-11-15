from Domain.librarie import getid, getgen, getpret, gettitlu, gettip_reducere
from Logic.CRUD import adauga_vanzare_carte, getByID, sterge_carte, modifica_carte


def test_adauga_vanzare_carte():
    lista = adauga_vanzare_carte('1', 'Me before you', 'romantic', 34.5, 'none', [])
    assert len(lista) == 1
    assert getid(getByID('1', lista)) == '1'
    assert getgen(getByID('1', lista)) == 'romantic'
    assert getpret(getByID('1', lista)) == 34.5
    assert gettitlu(getByID('1', lista)) == 'Me before you'
    assert gettip_reducere(getByID('1', lista)) == 'none'


def test_sterge_carte():
    lista = adauga_vanzare_carte('1', 'Me before you', 'romantic', 34.5, 'none', [])
    lista = adauga_vanzare_carte('2', 'Dialoguri socratice', 'filozofic', 51.33, 'silver', lista)
    lista = sterge_carte('1', lista)
    assert len(lista) == 1
    assert getByID('1', lista) is None

    try:
        lista = sterge_carte('3', lista)
        assert False
    except ValueError:
        assert len(lista) == 1
        assert getByID('2', lista) is not None
    except Exception:
        assert False


def test_modifica_carte():
    lista = adauga_vanzare_carte('1', 'Me before you', 'romantic', 34.5, 'none', [])
    lista = adauga_vanzare_carte('2', 'Dialoguri socratice', 'filozofic', 51.33, 'silver', lista)

    lista = modifica_carte('1', 'Spune-mi ce visezi', 'politist', 25.99, 'gold', lista)

    carteNoua = getByID("1", lista)
    assert getid(carteNoua) == "1"
    assert gettitlu(carteNoua) == 'Spune-mi ce visezi'
    assert getgen(carteNoua) == 'politist'
    assert getpret(carteNoua) == 25.99
    assert gettip_reducere(carteNoua) == 'gold'

    carte = getByID("2", lista)
    assert getid(carte) == "2"
    assert gettitlu(carte) == 'Dialoguri socratice'
    assert getgen(carte) == 'filozofic'
    assert getpret(carte) == 51.33
    assert gettip_reducere(carte) == 'silver'

    lista = []
    lista = adauga_vanzare_carte('1', 'Dialoguri socratice', 'filozofic', 51.33, 'silver', lista)
    try:
        lista = modifica_carte('3', 'Spune-mi ce visezi', 'politist', 25.99, 'gold', lista)
    except ValueError:
        carte = getByID("1", lista)
        assert getid(carte) == '1'
        assert gettitlu(carte) == 'Dialoguri socratice'
        assert getgen(carte) == 'filozofic'
        assert getpret(carte) == 51.33
        assert gettip_reducere(carte) == 'silver'
    except Exception:
        assert False


"""
def test_modificare_gen():
    lista = adauga_vanzare_carte('1', 'Me before you', 'romantic', 34.5, 'none', [])
    lista = adauga_vanzare_carte('2', 'Dialoguri socratice', 'filozofic', 51.33, 'silver', lista)

    lista = modifica_gen_carte('Me before you', 'drama', lista)

    carte = getByID('1', lista)
    assert getgen(carte) == 'drama'

    lista = adauga_vanzare_carte('1', 'Imaginea de ansamblu', 'experienta de viata', 34.99, 'silver', [])
    lista = adauga_vanzare_carte('2', 'Jurnalul unui pusti', 'comedie', 25, 'none', lista)
    lista = adauga_vanzare_carte('3', 'Spune-mi ce visezi', 'politist', 26.35, 'none', lista)

    lista = modifica_gen_carte('Spune-mi ce visezi', 'politist/romantic', lista)

    carte = getByID('3', lista)
    assert getgen(carte) == 'politist/romantic'

    lista = modifica_gen_carte('Spune-mi ce visezi', 'politist', lista)

    carte = getByID('3', lista)
    assert getgen(carte) == 'politist'

    lista = adauga_vanzare_carte('1', 'Me before you', 'romantic', 34.5, 'none', [])
    lista = adauga_vanzare_carte('2', 'Dialoguri socratice', 'filozofic', 51.33, 'silver', lista)
    try:
        lista = modifica_gen_carte('Mama', ' drama', lista)
    except ValueError:
        carte = getByID('1', lista)
        assert getgen(carte) == 'romantic'
    except Exception:
        assert False
"""