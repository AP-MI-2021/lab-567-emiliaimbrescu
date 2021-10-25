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

    lista = sterge_carte('3', lista)
    assert len(lista) == 1
    assert getByID('2', lista) is not None


def test_modifica_carte():
    lista = adauga_vanzare_carte('1', 'Me before you', 'romantic', 34.5, 'none', [])
    lista = adauga_vanzare_carte('2', 'Dialoguri socratice', 'filozofic', 51.33, 'silver', lista)

    lista=modifica_carte('1', 'Spune-mi ce visezi', 'politist', 25.99, 'gold', lista)

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
    assert getpret(carte) ==  51.33
    assert gettip_reducere(carte) == 'silver'

    lista = []
    lista = adauga_vanzare_carte('1', 'Dialoguri socratice', 'filozofic', 51.33, 'silver', lista)

    lista = modifica_carte('3', 'Spune-mi ce visezi', 'politist', 25.99, 'gold', lista)

    carte = getByID("1", lista)
    assert getid(carte) == '1'
    assert gettitlu(carte) == 'Dialoguri socratice'
    assert getgen(carte) == 'filozofic'
    assert getpret(carte) == 51.33
    assert gettip_reducere(carte) == 'silver'
