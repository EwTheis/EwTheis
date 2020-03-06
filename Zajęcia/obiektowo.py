class Stol(): #object
    def __init__(self):
        self.ilosc_nog = 4
    def __add__(self, other):
        return self.ilosc_nog + other.ilosc_nog

class Krzeslo():
    def __init__(self, kolor_siedziska = "czerwony",cena =100):
        self.kolor_siedziska = kolor_siedziska
        self.ilosc_kol = 5
        self.ilosc_nog = 5
        self.wysokosc = 90
        self.szerokosc = 40
        self.glebokosc = 40
        self.regulacja_wyskosci = True
        self.regulacja_podlokietnikow = False
        self.material = '100% cotton'
        self.cena =cena
        self.vat=22

    def __str__ (self):
        return f'Krzesło koloru: {self.kolor_siedziska}'

    def __lt__(self,other):
        return False

    def __len__(self):
        return 100000

    def pobierz_cene_netto(self):
        return self.cena
    
    def pobierz_cene_brutto(self):
        return self.cena * (1+self.vat/100)


krzeslo=Krzeslo()
print(krzeslo)
stol=Stol()
print(stol)

print(stol+krzeslo)



obiekt=Krzeslo('niebieski')
print(obiekt.pobierz_cene_netto())
print(obiekt.pobierz_cene_brutto())

obiekt2=Krzeslo('zielone',120)
print(obiekt2.pobierz_cene_netto())

print(obiekt2.cena * 1.22)

print(obiekt2.pobierz_cene_brutto())
