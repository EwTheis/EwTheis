import datetime

import tools as tools

class Ksiega():
    def __init__(self):
        self.nazwa = 'Ksiega Gosci'
        self.plik = 'book.pkl'

    def dodaj_wpis(self, wpis):
        self.wpisy.append(wpis)

    def zapisz(self):
        with open ()


class Wpis():
    def __init__(self, autor, tytul, tresc, data=None): #konstruktor
        self.autor = None #wlasciwosci klasy
        self.tresc = None
        self.data = None
        self.tytul = None
        if data is None:
            self.data = tools.dzis()
        else:
            self.data = data