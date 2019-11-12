# print("-" * 20 + " CSV " + "-" * 20)
#
# # odczyt, operacje i zapis na plikach CSV
# import csv
#
# with open("test.csv", "r+") as csv_file:
#     csv_data = csv.reader(csv_file)
#     sum = 0
#     for row in csv_data:
#         if (row[4].isdigit()):
#             age = int(row[4])
#             sum = sum + age
#     print(f"Wiek: {sum}")
#
#     csv_write = csv.writer(csv_file)
#     csv_write.writerow(["Łukasz", "Falkowicz, Kowalski", "Gdańsk", "12312313", "18"])
#

print("-" * 20 + " PICKLE " + "-" * 20)

# odczyt, operacje i zapis na plikach PICKLE
import pickle

entries = [
    {"title": "Pierwszy wpis", "body": "Treść pierwszego wpisu", "author": "Łukasz", "date" : "2019-11-07"},
    {"title": "Drugi wpis", "body": "Treść drugiego wpisu", "author": "Kasia", "date" : "2019-11-08"}
]

# Program pyta uztkownika o tytul, treść i imię
# dodaje wpis do książki
# wyświetla informację ile wpisów znajduje się w ksiazce

#1
title = input("Podaj tytuł:")
body = input("Podaj treść:")
author = input("Podaj imię:")

#2
new_entry = {"title": title, "body": body, "author": author, "date": "2019-11-07"}

#3
with open("book.pkl", "rb+") as book_file:
    try:
        old_entries = pickle.load(book_file)
    except:
        old_entries = []
    #4
    old_entries.append(new_entry)
    #5
    counter = len(old_entries)
    #6
    book_file.seek(0)
    pickle.dump(old_entries, book_file)
    #7
    print(f"Ilosc wpisów: {counter}")
    #8
    print("Dzięki")

print("-" * 20 + " Wyjątki " + "-" * 20)
# obsługa/łapanie wyjątków

try:
    division = 10 / 0
    print(unresolved_variable)
except ZeroDivisionError:
    print("Nie dziel przez zero")
except NameError:
    print("Brakuje zmiennej")
except:
    print("Nie wiem co się stało")



# CSV = COMMA SEPARATED VALUES
# domyślnym znakiem rozdzielnającym jest przecinek
# cudzysłów esc drugim cudysłowiem
# csv to biblioteka do czytania csv i rozwiązuje problemy z formatowaniem
# KONSTRUKCJA I KOMENDY
# import csv
# with open('adresy.csv', newline='') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         print(row)  # wyświetlanie zawartości
#     writer = csv.writer(csvfile)  # zapis do pliku
#     writer.writerow(['Jan', 'Kowlaski', 'Sopot', '123-432-111'])  # dopisuje do pliku

# PRZYKŁAD 1 - sumowanie wieku
# import csv
#
# imie = 0
# nazwisko = 1
# adres = 2
# telfon = 3
# wiek = 4
#
# with open('test.csv', 'r+', newline='') as csv_file:
#     csv_data = csv.reader(csv_file)
#
#     wiek_suma = 0
#
#     for row in csv_data:
#         # wiek = 4
#         if (row[4].isdigit()):  # pierwszy wiersz nie jest liczbą, bo to nazwa kolumny "wiersz", dopiero następne pozycje to liczby
#             wiek = int(row[4])  # można to sobie nazwać tak: print(row[wiek])
#             wiek_suma = wiek_suma + wiek
#     print(wiek_suma)
#
#     csv_write = csv.writer(csv_file)
#     csv_write.writerow(['Lukasz', 'Falkowicz', 'Gdansk', '365-364-635', '32'])

# PICKLE
import pickle

entries = [
    {"title": "Pierwszy wpis", "body": "Tesc pierwszego wpisu", "author": "Lukasz", "date": "2019-11-07"},
    {"title": "Drugi wpis", "body": "Tesc pierwszego wpisu", "author": "Lukasz", "date": "2019-11-07"}
]

# program pyta użytkoniwka o tytul, tresc i imie
# dodaje wpis do ksiazki
# wyswietla informacje ile wpisow znajduje sie w ksiazce

# 1 program pyta użytkoniwka o tytul, tresc i imie
title = input("Podaj tytuł: ")
body = input("Podaj treść: ")
author = input("Podaj autora: ")
date = '2019-11-07'

# 2 tworzy słownik
new_entry = {"title": title, "body": body, "author": author, "date": date}
print(new_entry)

# 3 otwieranie pliku i odczytujemy stare wpisy
with open('book.pkl', 'rb+') as book_file: # lista to typ binarny, więc musimy dać 'wb' albo 'rb+'
    # pickle.dump(new_entry, book_file)  # dump to zapisz - trzeba to zrobić na poczatku żeby plik nie był pusty
    old_entries = pickle.load(book_file)
    print(old_entries)
    # 4 dodanie nowego wpisu
    try:
        old_entries.append(new_entry)
    except:
        old_entries = []
    print(old_entries)
    # 5 policz ilość wpisów
    counter = len(old_entries)
    # 6 połącz
    book_file.seek(0)
    pickle.dump(old_entries, book_file)  # dump to zapisz
    # 7 wyświetl ilość wpisów
    print(counter)
    # 8
    print("Dzięki")


# # PROBLEMY
# try:  # try zatzrymuje się na 1 wyjątku
#     division = 10 / 0
#     print(unresolved_variable)
# except ZeroDivisionError:
#     print('Nie dziel przez 0')
# except NameError:
#     print('Brakuje zmiennej')
# except:
#     print('Nie wiem co sie stało')