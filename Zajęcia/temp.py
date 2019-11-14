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


from bs4 import BeautifulSoup
import requests

page = requests.get('https://wallpaperlist.com/')
parser = BeautifulSoup(page.content, "html.parser")
images = parser.find_all('img')

for image in images:
    print(image['src'])


 # file_name = page.split('/')[-1])
