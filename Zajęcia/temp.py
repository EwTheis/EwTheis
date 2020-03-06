#
#
# days=['poniedzialek', 'wtorek', 'sroda', 'czwartek', 'piatek', 'sobota', 'niedziela']
# weekend =('sobota', 'niedziela')
#
# for day in days:
#     if day in weekend:
#         print('jest week')
#     else:
#         print('praca')

# from PIL import Image
#
# image : Image.Image = Image.open('/home/kursant/Pobrane/fb_icon_325x325.png')
#
# image = image.resize((1064,1064))
# image = image.rotate(90)
#
#
# image.save('/home/kursant/Pobrane/fb_icon_64x64.png')
#
# import requests
#
# api_key = '800101cc05e0bcd5b88c816246c988ff'
# api_host ='http://api.openweathermap.org/data/2.5/weather'
# city = 'Gdansk'
#
# result = requests.get(f'{api_host}?appid={api_key}&q={city}')
#
# dict = result.json()
# print(f"temperatura: {dict['main']['temp']}")
# print(f"wiatr: {dict['wind']['speed']}' m/s")
# pass

# from bs4 import BeautifulSoup
# import requests
#
# page = requests.get('https://wallpaperlist.com/')
# parser = BeautifulSoup(page.content, "html.parser")
# images = parser.find_all('img')
#
# for image in images:
#     print(image['src'])



# 1. sciagnij wszystkei obrazki ze strony glownej wallpaperlist3.com do katalogu images.
# 2. zrob miniaturki obrazkow w katalogu images/thumbs o rozmiarach 64 px (szerokosc, a wys. proporcjonalna
# 3. policz ile jest zdjec na stronie
# 4. wyslij emaila z informacja ile zdjec sciagnieto, jaki jest sumaryczny rozmiar zdjec w MB i jaka jest pogoda w gdansku a)ile mb zaoszczedzilem robiac miniaturke
# 5. dopisz w mailu jaka jest pogoda w gda
#
#
# from bs4 import BeautifulSoup
# import requests
#
# page = requests.get('https://wallpaperlist.com/')
# parser = BeautifulSoup(page.content, "html.parser")
# images = parser.find_all('img')
#
# for image in images:
#     print(image['src'])
#
#
# import urllib.request
#
# urllib.request.urlretrieve("https://wallpaperlist.com/blue-blue-sea-ocean-13788", "local-filename.jpg")
#
#  # file_name = page.split('/')[-1])




# import folium
#
# map = folium.Map(location=[54.5236, 16.6750], zoom_start=3)
#
# tooltip = 'Kliknij mnie'
#
# rowery = [
#     {'geo': [54.5236, 16.6750], 'battery': 100},
#     {'geo': [52.5236, 13.6750], 'battery': 0},
#     {'geo': [51.5236, 14.6750], 'battery': 100}
# ]
#
# for rower in rowery:
#     popup = f"Bateria {rower['battery']}%"
#     if (rower['battery'] < 30):
#         color = 'red'
#     else:
#         color = 'blue'
#
#     marker = folium.Marker(
#         rower['geo'],
#         popup=popup,
#         tooltip=tooltip,
#         icon=folium.Icon(color=color, icon='info-sign')
#     )
#     marker.add_to(map)
#
# map.save('index.html')
#
# #
# class Stol():
#     def __init__(self):
#         self.ilosc_nog = 4
#
#     def __add__(self, other):
#         return self.ilosc_nog + other.ilosc_nog
#
# class Krzeslo():
#     def __init__(self, kolor_siedziska = "czerwony", cena = 100):
#         self.kolor_siedziska = kolor_siedziska
#         self.ilosc_kol = 5
#         self.ilosc_nog = 5
#         self.wysokosc = 90
#         self.szerokosc = 40
#         self.glebokosc = 40
#         self.regulacja_wyskosci = True
#         self.regulacja_podlokietnikow = False
#         self.material = '100% cotton'
#         self.cena = cena
#         self.vat = 23
#
#     def __str__(self):
#         return f'Krzesło koloru: {self.kolor_siedziska}'
#
#     def __lt__(self, other):
#         return False
#
#     def __len__(self):
#         return 100000
#
#     def pobierz_cene_netto(self):
#         return self.cena
#
#     def pobierz_cene_brutto(self):
#         return self.cena * (1 + self.vat/100)
#
# krzeslo = Krzeslo()
# print(krzeslo)
# stol = Stol()
# print(stol)
# stol.jakas_funkcja()
#
# print(stol + krzeslo)
# # #
# # # obiekt_2 = Krzeslo('zielone', 120)
# # # print(obiekt_2.pobierz_cene_netto())
# # # print(obiekt_2.cena)
# # #
# # # print(obiekt_2.pobierz_cene_brutto())
# # # print(obiekt_2.cena * 1.22)
# #
# # #print(obiekt.kolor_siedziska)
# # #print(print(obiekt))
# # #print(len(obiekt))
# # #print(obiekt < obiekt)
#
# class Zwierze():
#     def __init__(self):
#         self.oczy = 2
#         self.wlosy = True
#
#     def __str__(self):
#         return f'Oczy: {self.oczy}, włosy: {self.wlosy}'
#
# class Czlowiek(Zwierze):
#     def __init__(self):
#         super().__init__()
#
#     def czy_wlosy(self):
#         print('Mam wlosy')
#
#     def dajglos(self):
#         print('Hęęę')
#
# class Dresiarz(Czlowiek):
#     def __init__(self):
#         super().__init__()
#         self.wlosy = False
#
#     def dajglos(self):
#         print('Masz jakiś problem?')
#
# dresiarz = Dresiarz()
# dresiarz.dajglos()
# dresiarz.czy_wlosy()
# print("Nie mam:P")
# print(dresiarz)
#
#
#
# class Student(Czlowiek):
#     def dajglos(self):
#         print('Siema jestem student')
#
# class Kot(Zwierze):
#     def dajglos(self):
#         print('Miau')
#
# class Pies (Zwierze):
#     def dajglos(self):
#         print('Łuf... Łuf...')
#
# class Jamnik(Pies):
#     pass
#
# class Bokser(Pies):
#     pass
#
#
# # jamnik = Jamnik()
# # jamnik.dajglos() #z Psa
# # print(jamnik.oczy) #ze Zwierzęcia


#
# class A():
#     def hi(self):
#         print('A')
# class B(A):
#     # def hi(self):
#     #     print('B')
#     pass
# class C(A):
#     def hi(self):
#         print('C')
#     pass
# class D(B, C):
#     # def hi(self):
#     #     print('D')
#     pass

# D().hi()
# B().hi()
# C().hi()
# A().hi()