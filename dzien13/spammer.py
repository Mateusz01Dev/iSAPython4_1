from tools.poczta import Poczta
from dzien7.secrets import *

spammer = Poczta(login, haslo)

fotka = "../tools/smiley.jpg"
fotki = [fotka]

odbiorcy = [login]
temat = "Helloł from Arek"
tresc = "To są pliczki moje."
spammer.wyslij_wiadomosc(odbiorcy, temat, tresc, fotki)
