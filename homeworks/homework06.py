##########3statystyki dla pliku pan_tadeusz.txt

with open('statystykipliku.txt', 'a+') as file:
    file.seek(0)
    linia = file.readline()
    linia = linia[30:]
    linia_liczba = int(linia)+1
    file.truncate(30)
    file.write(f'{linia_liczba}')
    print(f'ilość uruchomień: {linia_liczba}')

with open('pan_tadeusz.txt', 'r+') as PT:
    PT = PT.read()
    ile_zdan = PT.count('.')
    ile = f'zdań jest {ile_zdan}'
    print(ile)

#zapisujemy wynik do pliku txt
with open('statystykipliku.txt', 'a+') as file:
    file.write(f'\n{ile}')
    podzial_tekstu = PT.split()
    licznik_slow = len(podzial_tekstu)
    ile_wyrazow = f'słów jest {licznik_wyrazow}'
    print(ile_wyrazow)

with open('statystykipliku.txt', 'a+') as file:
    file.write(f'\n{ile_wyrazow}')

##to Pan Tadeusz - tam nie ma liczb ;)

licz_liczby = 0
for slowo in podzial:
    for znak in slowo:
        cyfra = 0
        if znak.isdigit() is True:
            cyfra += 1
    if cyfra >= 1:
        licz_liczby += 1

licz_liczby = f'liczb jest {licz_liczby}'
print(licz_liczby)

with open('statystyki.txt', 'a+') as file:
    file.write(f'\n{licz_liczby}')