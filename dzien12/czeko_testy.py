from unittest import TestCase
from dzien10.czekolada import Czekolada
from tools.catch_print import *

class CzekoTesty(TestCase):

    def test_podaj_wage(self):
        czekolada = Czekolada("wedel", "mleczna", 150)
        oczekiwana_waga = 150

        rzeczywista_waga = czekolada.podaj_wage()

        self.assertEqual(rzeczywista_waga, oczekiwana_waga)

    def test_podaj_producenta(self):
        czekolada = Czekolada("wedel", "mleczna", 150)
        oczekiwany_prod = "wedel\n"

        rzeczywisty_prod = get_print_output(czekolada.podaj_producenta)

        self.assertEqual(rzeczywisty_prod, oczekiwany_prod)
