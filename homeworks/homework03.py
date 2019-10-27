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
