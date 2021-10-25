from Domain.librarie import creeazavanzare_carte, getid, gettitlu, getgen, getpret, gettip_reducere


def testcarte():
    carte = creeazavanzare_carte('1', 'Me before you', 'romantic', 34.5, 'none')
    assert getid(carte) == '1'
    assert gettitlu(carte) == 'Me before you'
    assert getgen(carte) == 'romantic'
    assert getpret(carte) == 34.5
    assert gettip_reducere(carte) == 'none'
