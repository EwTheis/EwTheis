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
#zakupy = ["kielbasa", "piwko", "chipsy", "wegiel", "kubeczki"]
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
# print("Kalkulator temp")
#
# liczba = input("Podaj w jakiej skali chcesz wprowadzić temp wejściową [F/C]: ")
#
# liczba=liczba.upper()
#
# if liczba == "C":
#     wprowadz_liczbe = int(input("Podaj stopnie w C: "))
# elif liczba == "F":
#     wprowadz_liczbe = int(input("Podaj stopnie w F: "))
# else:
#     print("wybrałeś złą skalę")
#
# if  liczba == "C" and wprowadz_liczbe in [0,100]:
#     St_F=32+(9/5)*wprowadz_liczbe
#     print("To jest " + str(St_F) + " stopni F")
# elif liczba == "F" and wprowadz_liczbe in [32,212]:
#     St_C=(5/9)*(wprowadz_liczbe-32)
#     print("To jest " + str(St_C) + " stopni C")
# else:
#     print("Wprowadziłeś błędną wartość")
#
# print("Koniec")


# print("Pierwsza i ostatnia cyfra")
#
# liczba = input("Podaj liczbę: ")
#
# if liczba >= "10":
#     print("Pierwsza cyfra podanej liczby to: " + liczba[0])
#     print("Ostatnia cyfra podanej liczby to: " + liczba[-1])
# else:
#     print("wprowadziłeś za małą liczbę")
#
# print("Koniec obliczeń")


# print("Sprawdzenie czy rok jest rokiem przestępnym")
#
# rok = int(input("Podaj rok, żeby sprawdzić czy jest przestępny: "))
#
# if rok % 4 == 0 and (rok % 100 != 0 or rok % 400 ==0):
#     print("Rok " + str(rok) + " jest przestępny")
# else:
#     print("Rok " + str(rok) + " nie jest przestępny")
#
# print("Koniec obliczeń")

# print("Przeliczanie wieku psa")
#
# wiek_ludzki = int(input("Podaj wiek człowieka: "))
# wiek_psa_przez_2lata=float(10.5)
# wiek_psa_pozostały=int(4)
# if wiek_ludzki <= 2:
#     wiek_psa= float((wiek_ludzki) * (wiek_psa_przez_2lata))
#     print(wiek_psa)
#     print(str(wiek_ludzki) + " ludzkich lat, to " + str(wiek_psa) + " psie lata")
#
# elif wiek_ludzki >= 3:
#     wiek_psa= float((wiek_ludzki-2)*wiek_psa_pozostały + wiek_psa_przez_2lata*2)
#     print(wiek_psa)
#     print(str(wiek_ludzki) + " ludzkich lat, to " + str(wiek_psa) + " psie lata")
#
# else:
#     print("coś poszło nie tak")
#
# print("koniec")