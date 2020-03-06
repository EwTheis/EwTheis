from book.model import Wpis
from book.model import Ksiega
import book.view as View

View.menu()
opcja = input('Mój wybór:')
ksiega = Ksiega()

if opcja == '1':
    autor = input('Jak masz na imie: ')
    tresc = input('Podaj treść wpisu: ')
    tytul = input('Podaj tytuł wpisu: ')

    wpis = Wpis(autor, tresc, tytul)
    ksiega.dodaj_wpis(wpis)
    rozmiar = len(ksiega)

    View.pokaz_rozmiar(rozmiar)
elif opcja == '2':
    wszystkie_wpisy = ksiega.wpisy
    View.pokaz_wpisy(wszystkie_wpisy)
else:
    View.blad()

