from Tests.testCRUD import test_adauga_vanzare_carte, test_sterge_carte
from Tests.testdomain import testcarte


def run_all_tests():
    testcarte()
    test_adauga_vanzare_carte()
    test_sterge_carte()
