def menu():
    print('Witaj w ksiedzegosci. Wybierz opcję:')
    print('1. Dodaj wpis')
    print('2. Pokaz wpisy')

def blad():
    print('Wystąpił bład')

def pokaz_rozmiar(rozmiar):
    print('Twoja księga ma: ' + str(rozmiar))

def pokaz_wpisy(wpisy):
    nr = 1
    for wpis in wpisy:
        print('-' * 20)
        print(f'Nr: {nr}')
        print(f'Autor: {wpis.autor}')
        print(f'Tytul: {wpis.tytul}')
        print('Treść: ' + wpis.parse_tresc())
        print(f'Treść skrócona: {wpis.parse_tresc(1)}')
        nr = nr + 1