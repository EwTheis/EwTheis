print('{:-^80}'.format('PĘTLE FOR'))

#petla po obiekcie range
liczby = range(0, 11)
for liczba in liczby:
    print(liczba)

#3 werianty iteracji po stringu

#wariant 1 - zamieniamy string na listę i iterujemy listę
napis = "Ala ma kota"
lista_z_napisu = list(napis)
for znak in lista_z_napisu:
    print(znak)

#wariant 2 - na podstawie długosci znaku odwołujemy się do każdej litery za pomocą indeksu
rozmiar = len(lista_z_napisu)
i=0
while(i < rozmiar):
    print(lista_z_napisu[i])
    i += 1

#wariant 3 (najleszy) - po prostu iterujemy po stringu
for znak in napis:
    print(znak)

#iteracja listy z dostępem do numerów indeksów
lista_imion = ['Ola', 'Ala', 'Tomek', 'Jan', 'Robert']

for i, imie in enumerate(lista_imion):
    print("Na pozycji: {} jest imie: {}".format(i, imie))

#iteracja po dwóch listach jednocześnie
lista_nazwiska = ['Kowalska', 'Malinowska', 'Iksiński', 'Igrekowski']
for imie, nazwisko in zip(lista_imion, lista_nazwiska):
    print("Mam na imie {} a moje nazwisko to {}".format(imie, nazwisko))


#string nie jest typem referencyjnym
napis = 'AAA'
przypisanie_napis = napis

napis = 'xxx'

print(napis)
print(przypisanie_napis)

#listy sa typem referencyjnym

print('{:-^80}'.format('COPY'))

import copy

lista = ['aaa', 'bbb', 'ccc', 'dddd']
print("Źródło:     " + str(lista))
przypisanie = lista

kopia_indeksami = lista[:]
kopia_konstruktorem = list(lista)
kopia_metoda = lista.copy()
kopia_biblioteka = copy.copy(lista)

lista[0] = 'XXX'

kopia_biblioteka[0] = 'YYY'

print("Lista:      " + str(lista))
print("Przypisanie:" + str(przypisanie))
print("Indeksy:    " + str(kopia_indeksami))
print("Konstruktor:" + str(kopia_konstruktorem))
print("Metoda:     " + str(kopia_metoda))
print("Biblioteka: " + str(kopia_biblioteka))

print('{:-^80}'.format('DEEPCOPY'))

lista2 = ['AAA', ['BBB', ['CCC', ['DDD']]]]
lista2_przypisanie = lista2

lista2_copy = copy.copy(lista2)
lista2_deepcopy = copy.deepcopy(lista2)

lista2_przypisanie[1][0] = 'YYY'

print("Lista:        " + str(lista2))
print("Przypisanie:  " + str(lista2_przypisanie))
print("Copy.copy:    " + str(lista2_copy))
print("Copy.deepcopy:" + str(lista2_deepcopy))

print('{:-^80}'.format('FUNKCJE'))

#definiowanie funkcji z parametrami różnego rodzaj
def wyswietl_napis(napis, koniec='.', poczek=''):
    do_wyswietlenia = str(poczek) + str(napis) + str(koniec)
    print(do_wyswietlenia)

zmienna_na_koniec = '!' * 20
wyswietl_napis('Ala', zmienna_na_koniec)

#funkcja zwracająca wartość
def znajdz_duze_liter(napis):
    zmienna = []
    for litera in napis:
        if(litera.islower()):
            zmienna.append(litera)
    return zmienna

wynik = znajdz_duze_liter('ZDanie Z dużyMi LiteRAmi')
print(wynik)


#funkcja z docstringiem pomocy
def policz_literke(litera="a", tekst="Ala ma kota"):
    """
    Funkcja która liczy ilosc danego znaku w tekscie i nie zwraca uwagi na wielkość danego znaku

    :param litera:
    :param tekst:
    :return:
    """

    # dzięki tym dwóm linijkom nie jest brana pod uwagę wilkość liter (case-insesitive)
    litera = litera.lower()
    tekst = tekst.lower()

    #wersja jednolinijkowa
    #return tekst.count()

    #wersja z użyciem for, if
    i = 0
    for litera_w_tekscie in tekst:
        if(litera_w_tekscie == litera):
            i += 1
    return i

print(policz_literke('z'))

print('>>> Pomoc do metody w stringach')
print(''.count.__doc__)

print('>>> Pomoć do naszej metody')
print(policz_literke.__doc__)

#nie każda funkcja musi coś zwracać, wtedy zwraca None
zmienna = print('TEST NA EKRANIE')
print(zmienna)


#PRACA DOMOWA - rozwiązanie
       #012345678901234567
dane = "215021482120211921002076207620502065202020152010200520002001199319901950183417501744186019462010"

dane[0:4] #0
dane[4:8] #1
dane[8:12] #2
dane[12:16] #3
dane[16:20] #4

for godzina in range(0,24):
     poczatek_zakresu = godzina * 4
     koniec_zakresu = poczatek_zakresu + 4
     temp = int(dane[poczatek_zakresu:koniec_zakresu]) / 100
     tab = ""

     if temp <= 18.5:
          tab = "\t!"
     elif temp <= 20:
          tab = "\t!!"

     wierz_string = f"{godzina}:00:\t {temp}\u00b0C{tab}"
     print(wierz_string)