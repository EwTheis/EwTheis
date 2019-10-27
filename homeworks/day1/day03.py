# # wiek = input("Ile masz lat? ")
# # zwierzaki = input("Ile masz kotów? ")
#
# wiek = 2
# zwierzaki = 5
#
# #zdanie = "Ala ma 2 lata i posiada 5 kotow"
#
# #zdanie = "Ala ma " + str(wiek) + " lata i posiada " + str(zwierzaki) + " kotow"
# #zdanie = f"Ala ma {wiek} lata i posiada {zwierzaki} kotow"
# #zdanie = "Ala ma {} lata i posiada {} kotow".format(wiek, zwierzaki)
# #zdanie = "Ala ma {a} lata i posiada {b} kotow".format(b=wiek, a=zwierzaki)
#
# liczba = 1.299
#
# print("liczba: %s" % liczba)
# print("liczba: %0.1f" % liczba)
# print("liczba: %d" % liczba)

#         012345678901
# zdanie = "encyklopedia"
#
# print(zdanie[4])
# print(zdanie[-3])
# print(zdanie[2:8])
# print(zdanie[:7])
# print(zdanie[8:])
# print(zdanie[7:1:-2])
# print(zdanie[::-1])

# print("Sprawdzanie parzystosci liczb")
# liczba = int(input("Podaj liczbę: "))
#
# if liczba % 3 == 0 and liczba % 5 == 0:
#     print("Podana liczba jest podzielna przez 3 i 5")
# elif liczba % 3 == 0:
#     print("Podana liczba jest podzielna przez 3")
# elif liczba % 5 == 0:
#     print("Podana liczba jest podzielna przez 5")
# else:
#     print("Podana liczba nie jest podizelna przez 3 i 5")
#
# print("Dzięki")

# wyrazy = ["raz", "dwa", "trzy"]
# wyrazy[0] = "jeden"
# print(wyrazy)

# liczby_parzyste = range(0,20,2)
# print(liczby_parzyste)
# if 40 in liczby_parzyste:
#     print("Prawda")
#
# lista_liczb_parzystych = list(range(0,20,2))
# print(lista_liczb_parzystych)
#
# lista_liczb_parzystych = tuple(range(0,20,2))
# print(lista_liczb_parzystych)
#
# napis = "dwa"
#
# lista = list("pierwszy")
# print(lista)
#
# lista = ['p', 'i', 'e', 'r', 'w', 's', 'z', 'y']
# print(lista)
# # #lista6 = list(1)
# # print(lista)
# # lista[0] = 'a'
# # print(lista)
# # napis[0] = 'a'
# # #print(lista5)
#
zakupy = ["kielbasa", "piwko", "chipsy", "wegiel", "kubeczki"]
#
# print(zakupy)
# zakupy.append("talerzyki")
# print(zakupy)
# zakupy.insert(0, "grill")
# print(zakupy)
# zakupy[0] = "elektryczny grill"
# zakupy.append("vodka")
# print(zakupy)
# if "vodka" in zakupy:
#     zakupy.remove("vodka")
# del(zakupy[0])
# print(zakupy)
# print(zakupy)

# lista = [ [1,2,3],[4,5,6],[7,8,9] ]
# lista = (
# 				[1,2,3],
# 				[4,5,6],
# 				[7,8,9]
# )
#
# lista[1][2] = 9
# print(lista)
#
# print("Start")
#
# zapytaj_ponownie = "T"
#
# while zapytaj_ponownie == "T":
#     zapytaj_ponownie_org = input("Czy zapytać ponownie? [T/N]")
#     zapytaj_ponownie = zapytaj_ponownie_org.upper()
#     print("Odpowiedziales: " + zapytaj_ponownie_org)
#
# print("Koniec")

for litera in "jakies zdanie":
    print(litera)

for przedmiot in zakupy:
    if przedmiot == 'piwko':
        znak = '[x] '
    else:
        znak = '[ ] '
    print(znak + przedmiot)