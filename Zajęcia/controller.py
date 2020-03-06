from ksiega_obiektowo import Wpis
from ksiega_obiektowo import Ksiega
import view as View

View.menu()
opcja = input('moj wybor:')

if opcja=='1':
    autor = input('Jak masz na imie: ')
    tresc = input ('Podaj tresc wpisu: ')
    tytul=input ('Podaj tytul wpisu: ')

    wpis=Wpis(autor, tresc, tytul)
    ksiega=Ksiega()
    ksiega.dodaj_wpis(wpis)

else:
    View.blad()