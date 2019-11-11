###########################1. Napisz program do przeliczania stopni Celsjusza na Fahrenheita i odwrotnie (wyświetlając wzór i kolejne obliczenia)
def Kalkulator_temp ():

    print("Kalkulator temp")

    liczba = input("Podaj w jakiej skali chcesz wprowadzić temp wejściową [F/C]: ")

    liczba=liczba.upper()
    if liczba == "C":
            wprowadz_liczbe = int(input("Podaj stopnie w C: "))
    elif liczba == "F":
            wprowadz_liczbe = int(input("Podaj stopnie w F: "))
    else:
            print("wybrałeś złą skalę")

    if  liczba == "C" and wprowadz_liczbe in [0,100]:
            St_F=32+(9/5)*wprowadz_liczbe
            print("To jest " + str(St_F) + " stopni F")
    elif liczba == "F" and wprowadz_liczbe in [32,212]:
            St_C=(5/9)*(wprowadz_liczbe-32)
            print("To jest " + str(St_C) + " stopni C")
    else:
            print("Wprowadziłeś błędną wartość")

    print("Koniec")

################################## 2. Napisz program, który poda pierwszą i ostatnią cyfrę podanej liczby
def Pierwsza_ostatnia_cyfra ():
    print("Pierwsza i ostatnia cyfra")

    liczba = input("Podaj liczbę: ")

    if liczba >= "10":
        print("Pierwsza cyfra podanej liczby to: " + liczba[0])
        print("Ostatnia cyfra podanej liczby to: " + liczba[-1])
    else:
        print("wprowadziłeś za małą liczbę")

    print("Koniec obliczeń")

################################## 3. Napisz program, który rysuje prostokąt o zadanych rozmiarach (wysokość i szerokość) za pomocą znaków | (bok) - (góra/dół) + (wierzchołek)

def Rysowanie_prostokąta ():
    szerokosc = "-"
    wysokosc = "|"
    l_szer = int(input("podaj szerokość prostokąta: "))
    l_wys = int(input("podaj wysokość prostokąta: "))
    print("+" + l_szer*szerokosc + "+")
    for i in range(0,l_wys):
            print(wysokosc + l_szer*" " + wysokosc)
    print("+" + l_szer*szerokosc + "+")

################################## 4. Napisz program do przeliczania liczby zapisanej w formacie binarnym na system dziesiętny.
def Przelicznik_liczby_na_binarną ():

    liczba_bin = input("podaj liczbę binarną:")
    liczba_dec = int(liczba_bin, 2)
    print(liczba_dec)


################################## 5. Napisz program do sprawdzania czy podany rok jest rokiem przestępnym
def Rok_przestępny ():
    print("Sprawdzenie czy rok jest rokiem przestępnym")

    rok = int(input("Podaj rok, żeby sprawdzić czy jest przestępny: "))

    if rok % 4 == 0 and (rok % 100 != 0 or rok % 400 ==0):
        print("Rok " + str(rok) + " jest przestępny")
    else:
        print("Rok " + str(rok) + " nie jest przestępny")

    print("Koniec obliczeń")


################################## 6.Stwórz program który przyjmie w parametrze dowolną listę np ['col1', 'col2', 'col3'] i wyświetli:
   # +------+------+------+
   # | col1 | col2 | col3 |
   # +------+------+------+
   # Dodatkowym atutem będzie gdy szerokość kolumn będzie zawsze równa bez względów na zawartość, tekst wyrównany do lewej.
   # Maksymalna szerokość kolumny np 30znaków jesli tekst będzie za długi niech zawartość przycina się i kończy trzema kropkami.
   # A jeszcze większym atutem będzie gdy będzie można podać liste zagnieżdżoną i narysuje się tabela z odpowiednią ilością wierszy i kolumn :)
#
def Owoce ():

    owoc1 = input("podaj 1. owoc")
    owoc2 = input("podaj 2. owoc")
    owoc3 = input("podaj 3. owoc")
    lista = [owoc1, owoc2, owoc3]
    # print("+" + len(owoc1)*"-" + "+" + len(owoc2)*"-" + "+" + len(owoc3)*"-" + "+")
    # print("|" + owoc1 + "|" + owoc2 + "|" + owoc3 + "|")
    # print("+" + len(owoc1)*"-" + "+" + len(owoc2)*"-" + "+" + len(owoc3)*"-" + "+")
    print("+" + 20*"-" + "+" + 20*"-" + "+" + 20*"-" + "+")
    print("|" + owoc1+(20-len(owoc1))*" " + "|" + owoc2+(20-len(owoc2))*" " + "|" + owoc3+(20-len(owoc3))*" " + "|")
    print("+" + 20*"-" + "+" + 20*"-" + "+" + 20*"-" + "+")


################################## 7. Program przyjmuje kwotę w parametrze i wylicza jak rozmienić to na monety: 5, 2, 1, 0.5, 0.2, 0.1 wydając ich jak najmniej.
def Wymiana_pieniedzy ():

    kwota_PLN = float(input("podaj kwotę do rozmienienia: "))

    if kwota_PLN <= 0:
        print("Błąd - nie rozmienisz pieniędzy, których nie masz ;)")
    else:
        piatki = kwota_PLN // 5
        dwojki = (kwota_PLN % 5) // 2
        jedynki = (kwota_PLN % 5 % 2) // 1
        piedziesieciogroszowki = (kwota_PLN % 5 % 2 % 1) // 0.5
        dwudziestogroszowki = (kwota_PLN % 5 % 2 % 1 % 0.5) // 0.2
        dziesieciogroszowki = (kwota_PLN % 5 % 2 % 1 % 0.5 % 0.2) // 0.1

    print("kwota", kwota_PLN, "składa się z: ")
    print("piątki: ", piatki)
    print("dwójki: ", dwojki)
    print("jedynki: ", jedynki)
    print("piędziesięciogroszówki", piedziesieciogroszowki)
    print("dwudziestogroszówki", dwudziestogroszowki)
    print("dziesięciogroszówki", dziesieciogroszowki)


################################## 8. Program rysujący piramidę o określonej wysokości, np dla 3
      #
     ###
    #####

def Piramida ():
    h_pir = int(input("podaj wysokość piramidy"))
    for i in range (0, h_pir):
        for j in range(0, h_pir-i-1):
            print(end=" ")
        for j in range(0, i+1):
            print("#", end=" ")
        print()


################################## 9. Kalkulator do wyliczania wieku psa. Przez pierwsze dwa lata, każdy psi rok to 10,5 ludzkiego roku, przez reszte lat psi rok to 4 ludzkie lata  Np: 15 ludzkich lat to 73 psie lata
def Kalkulator_wieku_psa ():

    print("Przeliczanie wieku psa")

    wiek_ludzki = int(input("Podaj wiek człowieka: "))
    wiek_psa_przez_2lata=float(10.5)
    wiek_psa_pozostały=int(4)
    if wiek_ludzki <= 2:
        wiek_psa= float((wiek_ludzki) * (wiek_psa_przez_2lata))
        print(wiek_psa)
        print(str(wiek_ludzki) + " ludzkich lat, to " + str(wiek_psa) + " psie lata")

    elif wiek_ludzki >= 3:
        wiek_psa= float((wiek_ludzki-2)*wiek_psa_pozostały + wiek_psa_przez_2lata*2)
        print(wiek_psa)
        print(str(wiek_ludzki) + " ludzkich lat, to " + str(wiek_psa) + " psie lata")

    else:
        print("coś poszło nie tak")

    print("koniec")


################################## 10. Zmienna dane zawiera 24 odczyty temperatury z 24 godzin. Każde 4 znaki to jeden odczyt w setnych stopni Celsjusza, tzn "2150" to 21.50°C Pomiary są dokonane o pełnych godzinach od 00:00 do 23:00. Wypisz do konsoli raport w formacie:
#
# <godzina>:<tabulator><stopnie z dokładnością do drugiego miejsca po przecinku><znak stopni>C
#
# Dla odczytów niższych niż lub równych 20°C dodaj "<tabulator>!" Dla odczytów niższych niż lub równych 18,5°C dodaj dodatkowy wykrzyknik. Nie kopiuj proszę znaku stopni. Spróbuj użyć znaku unicode \u00b0.
#
# dane = "215021482120211921002076207620502065202020152010200520002001199319901950183417501744186019462010"
# Przykład wyniku:
# (...)
# 20:00:  17.44°C    !!
# 21:00:  18.60°C    !
# 22:00:  19.46°C    !
# 23:00:  20.10°C
# (...)

#dodaj zeby było 01 i zakraglenia przy temp (k, f, d nawiasy)
def Odczyty_temp ():

    dane = "215021482120211921002076207620502065202020152010200520002001199319901950183417501744186019462010"
    dane[0:4]
    dane[4:8]
    dane[8:12]
    dane[12:16]
    dane[16:20]

    for godzina in range(0,24):
        poczatek_zakresu = godzina * 4
        koniec_zakresu = poczatek_zakresu + 4
        temp = int(dane[poczatek_zakresu:koniec_zakresu]) / 100
        zero = ""
        if godzina <=9:
            zero = "0"
        tab = ""
        if temp <=18.5:
            tab = "\t!"
        elif temp <=20:
            tab = "\t!!"
        wiersz_string = "{}{}:00:\t {:.2f}\u00b0C{}".format(zero,godzina,temp,tab)
        print (wiersz_string)

###pilot

# Zadania:
# 1) Prośba o przepisanie dotychczasowych proagramów z wykorzystaniem definiowania własnych funkcji i wytycznych powyżej
# 2) Stworzenie "programu nakładki" na dotychczasowe programiki.
#    Po wyborze danego programu z "menu" uruchomi się odpowiedni i po wykonaniu danej operacji zapyta czy wykonać inny program.
#    Sugeruje by każdy "podprogram był oddzielną funkcją".
#    Miejmy na uwadze to by w przyszłości ten program rozwijać podpinając kolejny "podprogram" - powinno to być najprostsze jak się da (np tylko zmiana menu i jakiegoś jednego ifa?:) )
#    Przykład przy uruchomieniu:
#    "
#    Witaj w Multitool Python Program by iSA - wersja beta ;)
#    Wybierz program który cię interesuje:
#    1) Rysowanie kwadratu o zadanych parametrach
#    2) Rysowanie piramidy o określonej wysokości
#    3) Rozmienianie pieniędzy
#    4) Przeliczanie F->C
#    5) Przeliczanie C->F
#    6) ...
#    7) ...
#    R) Wybierz program losowo bo nie wiem czego szukam:)
#    X) Wyjście z programu
#    Twój wybór: _
#    "


lista_programow = ["Witaj w Multitool. Wybierz program który cię interesuje: ",
                  "1) Rysowanie prostokątu o zadanych parametrach",
                  "2) Rysowanie piramidy o określonej wysokości",
                  "3) Przeliczanie C->F",
                  "4) Przeliczanie F->C",
                  "5) Pierwsza i ostatnia cyfra z liczby",
                  "6) Przeliczanie liczy binarnej na dziesiętną",
                  "7) Sprawdenie czy rok jest przestępny",
                  "8) Kalkulator do wyliczania wieku psa",
                  "9) Odczytywanie_temperatury",
                  "10) Rozmienianie pieniędzy",
                  "R) Wybierz program losowo bo nie wiem czego szukam:)",
                  "X) Wyjście z programu"]

zapytaj_ponownie = "T"
while zapytaj_ponownie == "T":
    print(f"\n".join(i for i in lista_programow) + "\n")  # rozdzielam elementy listy nową linią i kończę pustą linią
    wybor = input("Twój wybór: ")
    if wybor.isalpha():
        wybor_litera = wybor.upper()
        if wybor_litera == "R":
            from random import randint
            los = randint(1, 11)  # losowy wybór programu
            wybor = str(los)  # zamiana na str, ponieważ funkcja isdigit() w kolejnym if działa tylko dla str
            info = f"Wybrałeś losowy wybór programu. Przejdziesz teraz do zadania {wybor}\t"
        elif wybor_litera == "X":
            info = "Koniec. Dzięki, że tu zajrzałeś 😉"
            print(info)
            break
        else:
            info = "Twój wybór jest niepoprawny"
        print(info)
    if wybor.isdigit():
        lista_programow = int(wybor)
        if lista_programow == 1:
            Kalkulator_temp()
        elif lista_programow == 2:
            Pierwsza_ostatnia_cyfra()
        elif lista_programow == 3:
            Rysowanie_prostokąta()
        elif lista_programow == 4:
            Przelicznik_liczby_na_binarną()
        elif lista_programow == 5:
            Rok_przestępny()
        elif lista_programow == 6:
            Owoce()
        elif lista_programow == 7:
            Wymiana_pieniedzy()
        elif lista_programow == 8:
            Piramida()
        elif lista_programow == 9:
            Kalkulator_wieku_psa()
        elif lista_programow == 10:
            Odczyty_temp()
        else:
            info = "Twój wybór jest niepoprawny"
            print(info)
    zapytaj_ponownie = input("\nCzy chcesz uruchomić inny program? Wybierz [T/N]").upper()
    info = "Koniec. Dzięki, że tu zajrzałeś 😉"
    print(info)