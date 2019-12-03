import book.tools as tools
import pickle

class Ksiega():
    def __init__(self):
        self.nazwa = 'Ksiega Gości'
        self.plik = 'book.pkl'
        self.wpisy = []

        self.__odczyt() #tutaj laduje sopie wpisy :)

    def dodaj_wpis(self, wpis):
        self.wpisy.append(wpis)
        self.__zapis()

    def __zapis(self):
        with open(self.plik, "rb+") as plik_ksiegi:
            plik_ksiegi.seek(0)
            pickle.dump(self.wpisy, plik_ksiegi)

    def __odczyt(self):
        try:
            #plik istnieje wic czytam wszystkie wpisy z pliku
            plik_ksiegi = open(self.plik, "rb+")
            self.wpisy = pickle.load(plik_ksiegi)
        except:
            #nie ma pliku, ksiega jest pusta
            plik_ksiegi = open(self.plik, "wb+")

        plik_ksiegi.close()

    def __len__(self):
        return len(self.wpisy)

class Wpis():
    def __init__(self, autor, tytul, tresc, data=None):
        self.autor = autor
        self.tytul = tytul
        self.tresc = tresc
        if data is None:
            self.data = tools.dzis()
        else:
            self.data = data

    def parse_tresc(self, dlugosc=None):
        if dlugosc is None:
            return self.tresc
        else:
            return self.tresc[0:dlugosc] + '...'