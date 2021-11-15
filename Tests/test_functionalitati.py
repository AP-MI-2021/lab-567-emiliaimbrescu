from Domain.librarie import getpret, getgen
from Logic.CRUD import adauga_vanzare_carte, getByID
from Logic.functionalitati import aplicare_discount, modifica_genul, pret_minim, ordine_crescatoare, titluri_distincte


def test_aplicare_discount():
    lista = adauga_vanzare_carte('1', 'Tarot cu Mira', 'spiritual', 36.77, 'none', [])
    lista = adauga_vanzare_carte('2', 'Vara la bunici', 'aventura', 15, 'silver', lista)
    lista = adauga_vanzare_carte('3', 'Scripi', 'fantezie', 21.49, 'gold', lista)
    lista = aplicare_discount(lista)
    assert getpret(getByID('1', lista)) == 36.77
    assert getpret(getByID('2', lista)) == 14.25
    assert getpret(getByID('3', lista)) == 19.341


def test_modifica_genul():
    lista = adauga_vanzare_carte('1', 'Tarot cu Mira', 'spiritual', 36.77, 'none', [])
    lista = adauga_vanzare_carte('2', 'Vara la bunici', 'aventura', 15, 'silver', lista)
    lista = adauga_vanzare_carte('3', 'Scripi', 'fantezie', 21.49, 'gold', lista)
    lista = modifica_genul('Scripi', 'SF', lista)
    assert getgen(getByID('3', lista)) == 'SF'


def test_pret_minim():
    lista = adauga_vanzare_carte('1', 'Tarot cu Mira', 'spiritual', 36.77, 'none', [])
    lista = adauga_vanzare_carte('2', 'Vara la bunici', 'fantezie', 15, 'silver', lista)
    lista = adauga_vanzare_carte('3', 'Scripi', 'fantezie', 21.49, 'gold', lista)
    rezultat = pret_minim(lista)
    assert len(rezultat) == 2
    assert rezultat['spiritual'] == 36.77
    assert rezultat['fantezie'] == 15


def test_ordine_crescatoare():
    lista = []
    lista = adauga_vanzare_carte('1', 'Tarot cu Mira', 'spiritual', 36.77, 'none', lista)
    lista = adauga_vanzare_carte('2', 'Vara la bunici', 'fantezie', 15, 'silver', lista)
    lista = adauga_vanzare_carte('3', 'Scripi', 'fantezie', 21.49, 'gold', lista)
    lista = [carte[3] for carte in ordine_crescatoare(lista)]
    assert lista == [15, 21.49, 36.77]


def test_titluri_distincte():
    lista = adauga_vanzare_carte('1', 'Tarot cu Mira', 'spiritual', 36.77, 'none', [])
    lista = adauga_vanzare_carte('2', 'Vara la bunici', 'fantezie', 15, 'silver', lista)
    lista = adauga_vanzare_carte('3', 'Scripi', 'fantezie', 21.49, 'gold', lista)
    assert titluri_distincte(lista) == [('spiritual', 1), ('fantezie', 2)]
