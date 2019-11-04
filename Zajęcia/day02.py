#To jest zwykły komentarz
#print("Takie linie się nie wykonują")

#zapisywanie do zmiennej
zmienna = "Ala ma kota"

#przedrostek "r" - jeśli w stringu chcemy by znak \ był traktowany "dosłownie"
sciezka = r"c:\dokumenty\nowy folder\teren_1\tekst.txt"

#wyświetlenie na ekran
print("""Przywitanie
\"\"Łukasza\"\"
na kursie""")

#sprawdzanie typu
liczba_1_string = "1"
liczba_1_int = 1

print(type(liczba_1_int))
print(type(liczba_1_string))

#pobieranie danych od użytkownika i zmiana typu
wartosc_1 = input("Podaj licznbę 1: ")
wartosc_2 = input("Podaj licznbę 2: ")

#rzutowanie na liczbę: int(), lub ciąg znaków: str()
liczba_1 = int(wartosc_1)
liczba_2 = int(wartosc_2)

#operacje na różnych typach
print("Łączenie/konkatenacja:")
print(wartosc_1 + wartosc_2 * 3)
print("Dodawanie:")
print(liczba_1 + liczba_2)

#liczby zmiennoprzecinkowe
ulamek = 4.53
liczba_calkowita = 2

print(0.1 + 0.2)
print(ulamek * liczba_calkowita)

#wykonanie funkcji python
tekst = "Tytuł: Ala ma kotaz1!!!?"
dlugosc = len(tekst)
print(dlugosc)

#dostęp do znaków za pomocą slice'ingu
print(tekst[0])
print(tekst[11])
#print(tekst[23])

#wykonanie metod danego obiektu
print(tekst.upper())
print(tekst.capitalize())