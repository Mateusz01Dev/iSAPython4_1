from unittest import TestCase
from dzien12.kalkulator import *

class KalkulatorTesty(TestCase):

    def setUp(self):
        self.a = 23
        self.b = 34


    def test_dodaj(self):
        # arrange
        wynik_oczekiwany = self.a + self.b

        # act
        wynik_rzeczywisty = dodaj(self.a, self.b)

        # assert
        self.assertEqual(wynik_rzeczywisty, wynik_oczekiwany,
                         "Wartości obliczone są różne")

    def test_odejmij(self):
        # arrange
        wynik_oczekiwany = self.b - self.a

        # act
        wynik_rzeczywisty = odejmij(self.a, self.b)

        # assert
        self.assertEqual(wynik_rzeczywisty, wynik_oczekiwany)