from Tests.testCRUD import test_adauga_vanzare_carte, test_sterge_carte
from Tests.testUndoRedo import test_undo_redo
from Tests.test_functionalitati import test_aplicare_discount, test_modifica_genul, test_pret_minim, \
    test_ordine_crescatoare, test_titluri_distincte
from Tests.testdomain import testcarte


def run_all_tests():
    testcarte()
    test_adauga_vanzare_carte()
    test_sterge_carte()
    test_aplicare_discount()
    test_modifica_genul()
    test_pret_minim()
    test_ordine_crescatoare()
    test_titluri_distincte()
    test_undo_redo()
    print("Salut!")

