##########3statystyki dla pliku pan_tadeusz.txt
# otworzenie pliku ze statystyką i zapisanie kolejnego użycia pliku
#
#
# with open('statystykapliku.txt', 'a+') as file:
#     file.seek(0)
#     linia = file.readline()
#     linia = linia[10:]
#     linia_liczba = int(linia)+1
#     file.truncate(10)
#     file.write(f'{linia_liczba}')
#     print(f'ilość uruchomień: {linia_liczba}')


#zapisujemy wynik ile zdan do pliku txt
with open('pan_tadeusz.txt', 'r+') as PT:
    PT = PT.read()
    ile_zdan = PT.count('.')
    ile = f'Znalezionych zdań jest: {ile_zdan}'
    print(ile)

#zapisujemy wynik ile wyrazow do pliku txt
with open('statystykapliku.txt', 'a+') as file:
    file.write(f'\n{ile}')
    podzial_tekstu = PT.split()
    licznik_wyrazow = len(podzial_tekstu)
    ile_wyrazow = f'Znalezionych wyrazów jest: {licznik_wyrazow}'
    print(ile_wyrazow)
#
with open('statystykapliku.txt', 'a+') as file:
    file.write(f'\nZnalezionych wyrazów jest: {licznik_wyrazow}')

#### zlicz liczby w tekscie
liczba = 0
ile_liczb = 0
for slowo in ile_wyrazow:
    for litera in slowo:
        liczba = 0
        if litera.isdigit() is True:
            liczba += 1
    if liczba >= 1:
        ile_liczb += 1

licz_liczby = f'Znalezionych liczb jest: {ile_liczb}'
print(licz_liczby)

with open('statystykapliku.txt', 'a+') as file:
    file.write(f'\nZnalezionych liczb jest: {ile_liczb}')